
import streamlit as st

st.set_page_config(
    page_title="Strategic AI Studio",
    page_icon="🎯",
    layout="centered"
)

st.title("🎯 Strategic AI Studio")
st.subheader("Hindi Content Creation Toolkit")
st.write(
    "Apne YouTube video ke liye script, "
    "visual prompts aur title ideas taiyar karo."
)

topic = st.text_input(
    "Video topic likho",
    placeholder="Jaise: Ram Mandir Nirman"
)

format_type = st.selectbox(
    "Video format",
    ["YouTube Shorts", "Documentary"]
)

style = st.selectbox(
    "Visual style",
    [
        "Dark Cinematic Documentary",
        "3D Motion Graphics",
        "Satellite Map Animation",
        "Historical Reconstruction"
    ]
)

if st.button("Generate Content Pack"):
    if not topic.strip():
        st.warning("Pehle video topic likho.")
    else:
        st.header("Script Outline")
        st.write(
            f"Hook: {topic} ki ek aham kahani.\n\n"
            f"Context: {topic} ka background samjhein.\n\n"
            f"Main Story: Is topic ke important facts, "
            "events aur evidence explain karein.\n\n"
            "Conclusion: Darshakon se apni rai poochhein."
        )

        st.header("Visual Prompts")
        st.write(
            f"{style}, topic: {topic}. "
            "Cinematic lighting, detailed 3D visuals, "
            "dramatic camera movement, vertical 9:16."
        )

        st.header("YouTube Titles")
        st.write(f"{topic}: Puri Kahani")
        st.write(f"{topic} ke 3 Aham Pehlu")
        st.write(f"{topic}: Kya Jaanna Zaroori Hai?")

        st.download_button(
            "Download Content Pack",
            data=(
                f"TOPIC: {topic}\n"
                f"FORMAT: {format_type}\n"
                f"STYLE: {style}\n"
            ),
            file_name="strategic_content.txt"
        )

st.caption("Prototype v0.1 | Template-based output")
