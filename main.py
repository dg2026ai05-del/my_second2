import streamlit as st
import random
from streamlit_extras.let_it_rain import rain

st.set_page_config(page_title="가위바위보 대결 💕", page_icon="✊", layout="centered")

# 세션 상태 초기화
if "player_name" not in st.session_state:
    st.session_state.player_name = ""
if "player_score" not in st.session_state:
    st.session_state.player_score = 0
    st.session_state.com_score = 0
    st.session_state.rounds = 0
    st.session_state.player_choice = None
    st.session_state.com_choice = None
    st.session_state.result = ""
    st.session_state.game_started = False
    st.session_state.game_over = False

# 이름 입력 화면
if not st.session_state.game_started:
    st.title("💖 초귀여운 가위바위보 시작! 💖")
    st.subheader("너의 이름을 알려줘~ 🐰✨")
    
    name_input = st.text_input("이름 입력 (예: 하츄핑)", placeholder="내 이름은...")
    
    if st.button("🎮 게임 시작!", type="primary", use_container_width=True):
        if name_input.strip():
            st.session_state.player_name = name_input.strip()
            st.session_state.game_started = True
            st.rerun()
        else:
            st.warning("이름 꼭 써줘~ 😿")

else:
    name = st.session_state.player_name
    st.title(f"💕 {name}의 가위바위보 대결 💕")
    st.subheader(f"스코어: {st.session_state.player_score} : {st.session_state.com_score} (총 {st.session_state.rounds}판)")

    with st.expander("📜 규칙 보기", expanded=False):
        st.markdown("""
        - ✊ 바위 > ✌️ 가위  
        - ✌️ 가위 > 🖐️ 보  
        - 🖐️ 보 > ✊ 바위  
        - 같으면 비김 🤝  
        """)

    st.markdown("### 이번엔 뭐 낼까? 👀")
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("✊ 바위", use_container_width=True, type="primary", key="rock"):
            st.session_state.player_choice = "바위"

    with col2:
        if st.button("🖐️ 보", use_container_width=True, type="primary", key="paper"):
            st.session_state.player_choice = "보"

    with col3:
        if st.button("✌️ 가위", use_container_width=True, type="primary", key="scissors"):
            st.session_state.player_choice = "가위"

    if st.session_state.player_choice and not st.session_state.game_over:
        choices = ["바위", "보", "가위"]
        st.session_state.com_choice = random.choice(choices)

        player = st.session_state.player_choice
        com = st.session_state.com_choice

        st.markdown("---")
        st.subheader("결과~!")

        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown(f"**{name}** : {player} {'✊' if player=='바위' else '🖐️' if player=='보' else '✌️'}")
        with col_b:
            st.markdown(f"**상대** : {com} {'✊' if com=='바위' else '🖐️' if com=='보' else '✌️'}")

        if player == com:
            result = f"{name} 비겼어! 🤝"
            st.info(result, icon="🤝")
        elif (player == "바위" and com == "가위") or \
             (player == "보" and com == "바위") or \
             (player == "가위" and com == "보"):
            result = f"와아! {name} 이겼다! 🎉"
            st.success(result, icon="🏆")
            st.balloons()
            rain(emoji="💖", font_size=60, falling_speed=4, animation_length=3)
            st.toast(f"{name} 승리~ 야호!", icon="🏆")

<grok-card data-id="7b0399" data-type="image_card" data-plain-type="render_searched_image"  data-arg-size="LARGE" ></grok-card>



<grok-card data-id="cdf4fb" data-type="image_card" data-plain-type="render_searched_image"  data-arg-size="LARGE" ></grok-card>



<grok-card data-id="1fe082" data-type="image_card" data-plain-type="render_searched_image"  data-arg-size="LARGE" ></grok-card>

        else:
            result = f"아이고... {name} 졌네 ㅠㅠ"
            st.error(result, icon="😿")
            rain(emoji="😿", font_size=50, falling_speed=3, animation_length=2)

<grok-card data-id="44acb2" data-type="image_card" data-plain-type="render_searched_image"  data-arg-size="LARGE" ></grok-card>



<grok-card data-id="7fd8a6" data-type="image_card" data-plain-type="render_searched_image"  data-arg-size="LARGE" ></grok-card>



<grok-card data-id="bf0d6c" data-type="image_card" data-plain-type="render_searched_image"  data-arg-size="LARGE" ></grok-card>


        st.session_state.rounds += 1
        st.session_state.player_choice = None

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 또 한 판!", type="secondary", use_container_width=True):
            st.rerun()

    with col2:
        if st.button("🏁 그만하고 결과 보기!", type="primary", use_container_width=True):
            st.session_state.game_over = True
            st.rerun()

    if st.session_state.game_over:
        st.markdown("---")
        st.title("🏆 최종 결과 🏆")

        if st.session_state.player_score > st.session_state.com_score:
            st.success(f"축하해! {name}의 완승이야~ 🎉✨")
            st.balloons()
            rain(emoji="💖🌟", font_size=70, falling_speed=5, animation_length=5)
        elif st.session_state.player_score < st.session_state.com_score:
            st.error(f"이번엔 상대가 이겼네... ㅠㅠ 다음에 복수하자!")
            rain(emoji="😿💧", font_size=50, falling_speed=4, animation_length=4)
        else:
            st.info(f"무승부! {name}도 엄청 잘했어~ 🤝💕")

        st.metric("최종 스코어", f"{name} {st.session_state.player_score} : {st.session_state.com_score} 상대")

        st.subheader("🏅 오늘의 랭킹")
        st.write(f"1위: {name} ({st.session_state.player_score}승)")
        st.write(f"2위: 상대 ({st.session_state.com_score}승)")

        if st.button("🔄 새로 시작 (이름 다시)", type="primary"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
