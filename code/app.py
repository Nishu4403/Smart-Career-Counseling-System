from flask import Flask, render_template, request, redirect, url_for, send_file
import pickle

app = Flask(__name__)

# Load the model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Your feature list
features = ['Drawing', 'Dancing', 'Singing', 'Sports', 'Video Game', 'Acting', 'Travelling',
 'Gardening', 'Animals', 'Photography', 'Teaching', 'Exercise', 'Coding',
 'Electricity Components', 'Mechanic Parts', 'Computer Parts', 'Researching',
 'Architecture', 'Historic Collection', 'Botany', 'Zoology', 'Physics', 'Accounting',
 'Economics', 'Sociology', 'Geography', 'Psycology', 'History', 'Science',
 'Bussiness Education', 'Chemistry', 'Mathematics', 'Biology', 'Makeup', 'Designing',
 'Content writing', 'Crafting', 'Literature', 'Reading', 'Cartooning', 'Debating',
 'Asrtology', 'Hindi', 'French', 'English', 'Urdu', 'Other Language',
 'Solving Puzzles', 'Gymnastics', 'Yoga', 'Engeeniering', 'Doctor', 'Pharmisist',
 'Cycling', 'Knitting', 'Director', 'Journalism', 'Bussiness', 'Listening Music']

# Route: Main page
@app.route('/main')
def main():
    return render_template("main.html")

# NEW Route: Run logic when button is clicked
@app.route('/run_test', methods=['GET', 'POST'])
def run_test():
    print("Take Test button was pressed!")
    return redirect(url_for('index'))



# Route: Interest selection form
@app.route('/')
def index():
    return render_template("index.html", features=features)

@app.route('/mainfile')
def mainfile():
    return send_file("index.html")

# Route: Predict result
@app.route('/predict', methods=['POST'])
def predict():
    selected = request.form.getlist("features")
    input_vector = [1 if feature in selected else 0 for feature in features]
    prediction = model.predict([input_vector])[0]

    category_map = {
        0: 'Animation, Graphics and Multimedia',
        1: 'B.Arch- Bachelor of Architecture',
        2: 'B.Com- Bachelor of Commerce',
        3: 'B.Ed.',
        4: 'B.Sc- Applied Geology',
        5: 'B.Sc- Nursing',
        6: 'B.Sc. Chemistry',
        7: 'B.Sc. Mathematics',
        8: 'B.Sc.- Information Technology',
        9: 'B.Sc.- Physics',
        10: 'B.Tech.-Civil Engineering',
        11: 'B.Tech.-Computer Science and Engineering',
        12: 'B.Tech.-Electrical and Electronics Engineering',
        13: 'B.Tech.-Electronics and Communication Engineering',
        14: 'B.Tech.-Mechanical Engineering',
        15: 'BA in Economics',
        16: 'BA in English',
        17: 'BA in Hindi',
        18: 'BA in History',
        19: 'BBA- Bachelor of Business Administration',
        20: 'BBS- Bachelor of Business Studies',
        21: 'BCA- Bachelor of Computer Applications',
        22: 'BDS- Bachelor of Dental Surgery',
        23: 'BEM- Bachelor of Event Management',
        24: 'BFD- Bachelor of Fashion Designing',
        25: 'BJMC- Bachelor of Journalism and Mass Communication',
        26: 'BPharma- Bachelor of Pharmacy',
        27: 'BTTM- Bachelor of Travel and Tourism Management',
        28: 'BVA- Bachelor of Visual Arts',
        29: 'CA- Chartered Accountancy',
        30: 'CS- Company Secretary',
        31: 'Civil Services',
        32: 'Diploma in Dramatic Arts',
        33: 'Integrated Law Course- BA + LL.B',
        34: 'MBBS'
    }

    category_name = category_map.get(prediction, "Unknown Category")
    return render_template("result.html", result=category_name)

if __name__ == '__main__':
    app.run(debug=True)
