import os
import pandas as pd
import plotly.graph_objects as go
from fpdf import FPDF
from datetime import datetime

LOGO_PATH = "assets/logo.jpg"
OUTPUT_PATH = "reports/"

VERDE_ESCURO = (45, 106, 0)
VERDE_CLARO = (139, 195, 74)
CINZA = (102, 102, 102)
BRANCO = (255, 255, 255)


def gerar_graficos(df: pd.DataFrame) -> list:
    os.makedirs("reports/temp", exist_ok=True)
    caminhos = []
    graficos = [
        ("impressions", "Impressões","#2D6A00"),
        ("clicks", "Cliques", "#8BC34A"),
        ("spend", "Gastos", "#FFA726"),
    ]
    for coluna, titulo, cor in graficos:
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=df["date"],
            y=df[coluna],
            marker_color=cor,
            name=f"{titulo} por Dia",
        ))
        fig.update_layout(
            title=f"{titulo} por Dia",
            plot_bgcolor="lightgreen",
            width=700,
            height=350,)
        fig.write_image(f"reports/temp/{coluna}.png")
        caminhos.append(f"reports/temp/{coluna}.png")
    return caminhos

def gerar_pdf(insights: list) -> str:
    df = pd.DataFrame(insights)
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date")
    datamin = df["date"].min().strftime("%d/%m/%Y")
    datamax = df["date"].max().strftime("%d/%m/%Y")
    titulo = f"Relatório Semanal Meta ADS - {datamin} a {datamax}"
    imp =  df["impressions"].sum()
    clk = df["clicks"].sum()
    spd = df["spend"].sum()
    graficos = gerar_graficos(df)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_margins(15, 15, 15)
    pdf.image(LOGO_PATH, x=15, y=10, w=40)
    pdf.set_font("Arial", "B", 14)
    pdf.ln(35)
    pdf.set_text_color(*VERDE_ESCURO)
    pdf.cell(0, 10, titulo, ln=True, align="C")
