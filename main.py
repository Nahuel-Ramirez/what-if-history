import os
from openai import OpenAI
from dotenv import load_dotenv

# Cargar variables del .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def generar_rama_con_ia(historia_base, numero):
    prompt = f"""
Imaginá que estás escribiendo una historia alternativa. El hecho es: "{historia_base}".

Escribí una versión detallada de lo que habría pasado en esta línea temporal #{numero}.
Describí los eventos históricos clave, consecuencias políticas, tecnológicas y sociales.
No repitas el hecho base, empezá directamente con las consecuencias. Mantené un tono narrativo.

Línea temporal #{numero}:
"""

    respuesta = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Sos un historiador experto en universos alternativos."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.9,
        max_tokens=700
    )

    return respuesta.choices[0].message.content.strip()

def main():
    print("🕰️  Bienvenido a What If: Historia Alternativa")
    hecho = input("🔍 Ingresá un hecho histórico alternativo (ej: 'Hitler fue aceptado en la academia de arte'): ")

    print("\n🔮 Generando líneas temporales con IA...\n")

    for i in range(1, 4):
        rama = generar_rama_con_ia(hecho, i)
        print(f"🌐 Línea temporal #{i}:\n{rama}\n{'-'*60}\n")

if __name__ == "__main__":
    main()

