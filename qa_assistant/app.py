"""Web UI for AI QA Assistant using Streamlit."""

from __future__ import annotations

import streamlit as st

from agent import QAAssistantError, ask_agent


COMMANDS = [
    "/testcases",
    "/checklist",
    "/weakspots",
    "/negative",
    "/bugreport",
    "/http",
    "/interview",
    "/swagger",
    "/postman",
]


def main() -> None:
    st.set_page_config(
        page_title="AI QA Assistant",
        page_icon="🧪",
        layout="wide",
    )

    st.title("🧪 AI QA Assistant")
    st.write("Локальный AI-помощник для QA-инженера на Python + Ollama.")

    command = st.selectbox("Выбери команду", COMMANDS)

    user_input = st.text_area(
        "Описание задачи",
        placeholder='Например: POST /login email password',
        height=160,
    )

    if st.button("Сгенерировать"):
        if not user_input.strip():
            st.warning("Введи описание задачи.")
            return

        full_prompt = f"{command} {user_input}"

        with st.spinner("Генерирую ответ..."):
            try:
                answer = ask_agent(full_prompt)
            except QAAssistantError as error:
                st.error(str(error))
                return
            except Exception as error:
                st.error(f"Неожиданная ошибка: {error}")
                return

        st.subheader("Результат")
        st.markdown(answer)


if __name__ == "__main__":
    main()