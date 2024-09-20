import csv
quotes_data=[
    {"Quotes":"The person be it gentleman or lady who has not pleasure in a good novintolerably stupid","Author":"Jane Austen"},
    {"Quotes":"A day without sunshine is like,you know,night","Author":"Steve Martin"},
    {"Quotes":"Beauty from time to time to give a stupid or misinformed beholder a black eye.","Author":"Garrison kailor"},
    {"Quotes":"Beauty is in the eye of the beholder and it may be necessary from time to time to give a stupid or misinformed beholder a black eye.","Author":" Jim Henson"},
    {"Quotes":"All you need is love. But a little chocolate now and then doesn't hurt.", "Author": " Charles M schulz"},
    {"Quotes":"Remember, we're madly in love, so it's all right to kiss me anytime you feel like it.", "Author": "Suzzane collins "},
    {"Quotes":"Some people never go crazy. What truly horrible lives they must lead.", "Author": " Charles Bukowsi"},
    {"Quotes":"The trouble with having an open mind, of course, is that people will insist on coming along and trying to put things in it. ", "Author": "Terry Parcett "},
    {"Quotes":"Think left and think right and think low and think high. Oh, the thinks you can think up if only you try! ", "Author": " Dr suess"},
    {"Quotes":"The reason I talk to myself is because I’m the only one whose answers I accept.", "Author": "George Carlin "},
]
filename="output.csv"
with open(filename, mode='w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["Quotes", "Author"])
    # Write the header
    writer.writeheader()
    # Write the data
    for entry in quotes_data:
        writer.writerow(entry)

