import os
import pandas as pd
import plotly.graph_objects as go
from fpdf import FPDF
from datetime import datetime

LOGO_PATH = "assets/logo hnh.jpg"
OUTPUT_PATH = "reports/"

VERDE_ESCURO = (45, 106, 0)
VERDE_CLARO = (139, 195, 74)
CINZA = (102, 102, 102)
BRANCO = (255, 255, 255)


def gerar_graficos(df: pd.DataFrame) -> list:
    os.makedirs("reports/temp", exist_ok=True)
    caminhos = []
    graficos = [
        ("impressions", "Impressões", "#2D6A00"),
        ("clicks", "Cliques", "#8BC34A"),
        ("spend", "Gastos", "#FFA726"),
    ]
    for coluna, titulo, cor in graficos:
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=df["date"],
            y=df[coluna],
            marker_color=cor,
            name=titulo,
        ))
        fig.update_layout(
            title=titulo,
            plot_bgcolor="#e8f5e9",
            paper_bgcolor="white",
            width=750,
            height=280,
            margin=dict(l=40, r=20, t=40, b=60),
            xaxis=dict(tickformat="%d/%m", tickangle=-30),
        )
        fig.write_image(f"reports/temp/{coluna}.png")
        caminhos.append(f"reports/temp/{coluna}.png")
    return caminhos

def gerar_pdf(insights: list) -> str:
    df = pd.DataFrame(insights)
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date")
    datamin = df["date"].min().strftime("%d/%m/%Y")
    datamax = df["date"].max().strftime("%d/%m/%Y")

    imp = df["impressions"].sum()
    clk = df["clicks"].sum()
    spd = df["spend"].sum()
    conv = df["conversions"].sum()
    ctr_medio = round((clk / imp) * 100, 2) if imp > 0 else 0
    cpm_medio = round((spd / imp) * 1000, 2) if imp > 0 else 0
    cpl = round(spd / conv, 2) if conv > 0 else 0
    convvalue = df["revenue"].sum()
    roas = round(convvalue / spd, 2) if spd > 0 else 0

    graficos = gerar_graficos(df)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_margins(10, 10, 10)

    # --- CABEÇALHO VERDE COM LOGO E TÍTULO ---
    pdf.set_fill_color(*VERDE_ESCURO)
    pdf.rect(0, 0, 210, 30, "F")
    pdf.image(LOGO_PATH, x=5, y=3, h=24)
    pdf.set_xy(0, 8)
    pdf.set_font("Arial", "B", 11)
    pdf.set_text_color(*BRANCO)
    pdf.cell(210, 10, f"Relatório Meta ADS - {datamin} a {datamax}", align="C")

    # --- FAIXA OVERVIEW ---
    pdf.set_fill_color(*VERDE_ESCURO)
    pdf.rect(0, 33, 210, 12, "F")
    pdf.set_xy(0, 33)
    pdf.set_font("Arial", "B", 12)
    pdf.set_text_color(*BRANCO)
    pdf.cell(210, 12, "OVERVIEW GERAL DA CAMPANHA", align="C")

    # --- MÉTRICAS LINHA 1 ---
    metricas = [
        ("Impressões", f"{imp:,}"),
        ("Cliques", f"{clk:,}"),
        ("Gastos", f"R$ {spd:,.2f}"),
        ("Conversões", f"{conv:,}"),
        ("CTR Médio", f"{ctr_medio}%"),
        ("CPM Médio", f"R$ {cpm_medio:,.2f}"),
        ("CPL", f"R$ {cpl:,.2f}"),
        ("Receita", f"R$ {convvalue:,.2f}"),
        ("ROAS", f"{roas}"),
    ]
    metricas_linha1 = metricas[:6]
    metricas_linha2 = metricas[6:]

    pdf.set_draw_color(*VERDE_ESCURO)
    box_w = 31
    box_h = 18
    x_start = 10
    y_start = 48

    for i, (nome, valor) in enumerate(metricas_linha1):
        x = x_start + i * (box_w + 2)
        pdf.rect(x, y_start, box_w, box_h)
        pdf.set_xy(x, y_start + 2)
        pdf.set_font("Arial", "", 7)
        pdf.set_text_color(*CINZA)
        pdf.cell(box_w, 4, nome, align="C")
        pdf.set_xy(x, y_start + 8)
        pdf.set_font("Arial", "B", 9)
        pdf.set_text_color(*VERDE_ESCURO)
        pdf.cell(box_w, 6, valor, align="C")

    # --- MÉTRICAS LINHA 2 ---
    y_start2 = y_start + box_h + 4
    for i, (nome, valor) in enumerate(metricas_linha2):
        x = x_start + i * (box_w + 2)
        pdf.rect(x, y_start2, box_w, box_h)
        pdf.set_xy(x, y_start2 + 2)
        pdf.set_font("Arial", "", 7)
        pdf.set_text_color(*CINZA)
        pdf.cell(box_w, 4, nome, align="C")
        pdf.set_xy(x, y_start2 + 8)
        pdf.set_font("Arial", "B", 9)
        pdf.set_text_color(*VERDE_ESCURO)
        pdf.cell(box_w, 6, valor, align="C")

    # --- GRÁFICOS ---
    y_graficos = y_start2 + box_h + 6
    for caminho in graficos:
        pdf.image(caminho, x=10, y=y_graficos, w=190)
        y_graficos += 68

    os.makedirs(OUTPUT_PATH, exist_ok=True)
    saida = f"{OUTPUT_PATH}relatorio_{df['date'].min().strftime('%Y%m%d')}_{df['date'].max().strftime('%Y%m%d')}.pdf"
    pdf.output(saida)
    for caminho in graficos:
        os.remove(caminho)
    return saida