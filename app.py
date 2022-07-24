# streamlit app assignment TDS GA 8
# streamlit run "C:\Users\tusha\Jupyter_notebooks\IITM_Term_5\TDS\GA_8\app.py"

import streamlit as st

def is_number(x):
    x = str(x)
    if len(x)==0:return False
    for i in x:
        if i.isdigit() or i==".": continue
        else: return False
    return True
    
def main():
    st.write("""
    # Simple Addition App
    ### TDS : GA 8 : Streamlit app for addition of two numbers
    """)

    num_1 = st.text_input("Enter first number", value="0")
    num_2 = st.text_input("Enter second number", value="0")

    add = ""  
    if len(num_1)==0 and len(num_2)==0: add=""
    else: add="INVALID" 
    if is_number(num_1) and is_number(num_2): add = str(float(num_1) + float(num_2))

    st.write(f"""
    ### Addition: {num_1} + {num_2} = {add}
    """)

    st.write(f"")
    st.write(f"")
    st.write(f"")
    st.write(f"")
    st.write(f"")

    st.write(f"""
    ### Creator: Tushar Supe (21F1003637)
    """)

if __name__=='__main__':
    main()
# END