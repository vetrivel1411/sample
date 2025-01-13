from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Social Awareness Campaign</h1>
    <p>Welcome to our social awareness page. Below are some important messages:</p>
    <h2>1. Climate Change Awareness</h2>
    <p>Climate change is one of the biggest challenges facing our planet. It is important to take action, reduce carbon emissions, and adopt sustainable practices.</p>
    <h2>2. Mental Health Matters</h2>
    <p>Mental health is just as important as physical health. Reach out to loved ones and seek help if needed. Remember, you are not alone.</p>
    <h2>3. Support for Equality</h2>
    <p>Everyone deserves equal rights, regardless of race, gender, or background. Let’s work together to create a fair and just society.</p>
    <h2>4. Fighting Hunger</h2>
    <p>Millions of people around the world go hungry every day. You can contribute by supporting local food banks and charities.</p>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
