import streamlit as st
import pandas as pd

st.set_page_config(page_title = "Student analytics dashboard", layout="wide")

st.title("Smart Students Marks Analyzer")
st.caption("Visual insights * smart evaluation * Professinal reporting")

st.divider()

st.subheader("Enter Subject Marks")
st.write("Enter your marks to analyze performance")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    s1 = st.text_input("Subject 1")
    m1 = st.number_input("Marks for Subject 1", 0,100, key="m1")

with col2:
    s2 = st.text_input("Subject 2")
    m2=st.number_input("Marks for subject 2", 0, 100, key="m2")

with col3:
    s3 = st.text_input("Subject3")
    m3= st.number_input("Marks for subject 3", 0,100, key="m3")

with col4:
    s4 = st.text_input("Subject4")
    m4 = st.number_input("Marks for SUbject 4",0,100, key="m4")

with col5:
    s5 = st.text_input("Subject5")
    m5 = st.number_input("Marks for subject 5", 0,100,key="m5")

if st.button("Generate Dashboard"):
    subjects = [s1,s2,s3,s4,s5]
    marks = [m1,m2,m3,m4,m5]

    data = pd.DataFrame({"Subjects": subjects,
                         "Marks": marks})
    
    st.divider()
    st.subheader("Performance Visualizations")

    colA , colB = st.columns(2)

    with colA:
        st.write("### Bar Chart")
        st.bar_chart(data.set_index("Subjects"))
    with colB:
        st.write("### Pie Chart")
        st.pyplot(data.set_index("Subjects").plot.pie(y="Marks", autopct = "%1.1f%%", legend = False).figure)

    st.divider()

    avg = sum(marks)/len(marks)

    if avg >= 85:
        grade = "A+ 🌟"
    elif avg >= 70:
        grade = "A"
    elif avg >= 55:
        grade = "B"
    elif avg >= 40:
        grade = "C"
    else:
        grade = "Fail !"
    
    colX, colY, colZ = st.columns(3)

    colX.metric("Average Marks", f"{avg:.2f}")
    colY.metric("Grade", grade)
    colZ.metric("Subjects", len(subjects))

    best = data.loc[data["Marks"].idxmax()]
    weak = data.loc[data["Marks"].idxmin()]

    st.success(f"Best Subject: {best['Subjects']} with {best['Marks']} marks")
    st.error(f"Weak Subject: {weak['Subjects']} with {weak['Marks']} marks")

    st.subheader("Smart Suggestions")

    for i in range(len(subjects)):
        if marks[i] >= 75:
            st.write(f"{subjects[i]} - Excellent Mastery")
        elif marks[i] >= 50:
            st.write(f"{subjects[i]} - Practice more")
        else:
            st.write(f"{subjects[i]}) - Needs serious improvement")

    st.subheader("Overall Result")

    if avg >= 75:
        st.balloons()
        st.write("🌟 Outstanding Performance!")
    elif avg >= 50:
        st.write("👍 Good Progress - Keep going!")
    else:
        st.write("📚 Improvement Required - Don't give up!")