import datetime
import random
import numpy as np
import pandas as pd
import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="프리미엄 대시보드",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 커스텀 CSS 적용 (전반적인 UI 디자인 개선)
st.markdown(
    """
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .sidebar .stSidebarContent {
        background-color: #ffffff;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# 사이드바 설정
st.sidebar.title("🛠️ 제어판")
st.sidebar.markdown("---")

# 메뉴 선택
menu = st.sidebar.radio(
    "메뉴 이동", ["📊 실시간 대시보드", "📝 데이터 관리 및 분석", "⚙️ 설정"]
)

st.sidebar.markdown("---")
st.sidebar.subheader("🔍 필터 옵션")

# [오류 해결 부분] st.date_input에 튜플(시작일, 종료일)을 전달하여 기간 선택(Range) 구현
today = datetime.date.today()
start_default = today - datetime.timedelta(days=7)
date_range = st.sidebar.date_input(
    "조회 기간 선택", (start_default, today), format="YYYY-MM-DD"
)

category = st.sidebar.selectbox(
    "카테고리", ["전체", "IT/기술", "마케팅", "재무", "인사"]
)

# 메인 화면 로직
if menu == "📊 실시간 대시보드":
  st.title("📊 인터랙티브 비즈니스 대시보드")
  st.markdown(
      "환영합니다! 이 웹페이지는 파이썬 파일 하나(`app.py`)로 구동되는 고성능 대시보드입니다."
  )

  # 상단 지표(Metric) 카드 3개
  col1, col2, col3, col4 = st.columns(4)
  with col1:
    st.metric(
        label="총 방문자수", value="12,450명", delta="+12% (전주 대비)"
    )
  with col2:
    st.metric(label="매출액", value="45,200,000원", delta="+5.4%")
  with col3:
    st.metric(label="전환율", value="3.2%", delta="-0.4%")
  with col4:
    st.metric(label="고객 만족도", value="4.8 / 5.0", delta="+0.2")

  st.markdown("---")

  # 차트 영역
  st.subheader("📈 주간 트렌드 분석 차트")

  # 더미 데이터 생성
  chart_data = pd.DataFrame(
      np.random.randn(20, 3), columns=["방문자", "주문수", "이탈률"]
  )

  tab1, tab2 = st.tabs(["꺾은선 그래프", "막대 그래프"])

  with tab1:
    st.line_chart(chart_data)
  with tab2:
    st.bar_chart(chart_data)

elif menu == "📝 데이터 관리 및 분석":
  st.title("📝 데이터 관리 및 파일 분석")
  st.markdown("데이터셋을 확인하고 필터링 결과를 테이블로 확인하세요.")

  # 샘플 데이터프레임 생성
  @st.cache_data
  def load_data():
    names = ["김철수", "이영희", "박민수", "정지은", "강동원", "한지민"]
    departments = ["IT/기술", "마케팅", "재무", "인사", "IT/기술", "마케팅"]
    data = {
        "이름": [random.choice(names) for _ in range(20)],
        "부서": [random.choice(departments) for _ in range(20)],
        "성과점수": np.random.randint(70, 100, 20),
        "근무일수": np.random.randint(150, 300, 20),
        "등록일": [
            datetime.date.today() - datetime.timedelta(days=int(i))
            for i in np.random.randint(0, 30, 20)
        ],
    }
    return pd.DataFrame(data)


  df = load_data()

  # 데이터프레임 검색 및 필터링 기능
  search_query = st.text_input(
      "🔍 이름 검색", "", placeholder="이름을 입력하세요..."
  )
  if search_query:
    df = df[df["이름"].str.contains(search_query)]

  st.dataframe(df, use_container_width=True)

  # 데이터 다운로드 버튼
  csv = df.to_csv(index=False).encode("utf-8-sig")
  st.download_button(
      label="📥 CSV 파일로 다운로드",
      data=csv,
      file_name="filtered_data.csv",
      mime="text/csv",
  )

else:
  st.title("⚙️ 시스템 설정")
  st.markdown("웹페이지의 환경 설정을 관리합니다.")

  st.text_input("API 키 입력", type="password")
  st.checkbox("이메일 알림 받기", value=True)
  st.slider("데이터 새로고침 주기 (분)", 1, 60, 10)

  if st.button("설정 저장하기"):
    st.success("설정이 성공적으로 저장되었습니다!")

# 하단 푸터
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>© 2026 Single File Python Web App. Built with Streamlit.</p>",
    unsafe_allow_html=True,
)
#실행
# python -m streamlit run app.py
# python -m_streamlit_dashboard.py