# 1. Basis-Image
FROM python:3.11-slim

# 2. System-Tools (curl) für uv-Installation
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# 3. uv installieren
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:${PATH}"

# 4. Arbeitsverzeichnis
WORKDIR /app

# 5. Projekt-Metadaten zuerst kopieren (für Docker-Layer-Caching)
#   -> pyproject.toml + uv.lock gehören ins Repo
COPY pyproject.toml uv.lock* ./

# 6. Dependencies installieren (ohne Dev-Dependencies)
RUN uv sync --frozen --no-dev

# 7. Restlichen Code kopieren
COPY . .

# 8. Port konfigurieren (Standard für Streamlit; kann in ACA überschrieben werden)
ENV PORT=8501

# 9. Expose (dient nur der Doku, ACA nimmt targetPort aus der Konfiguration)
EXPOSE 8501

# 10. Startkommando: Streamlit-App aus main.py starten
CMD ["uv", "run", "streamlit", "run", "main.py", "--server.address=0.0.0.0", "--server.port=8501"]
