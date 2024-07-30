import tkinter as tk
from textblob import TextBlob
from newspaper import Article

def summarize():
    try:
        url = utext.get("1.0", "end").strip()  #strip(): Metindeki baştaki ve sondaki boşlukları temizler.
        art = Article(url)
        
        # Makaleyi indir
        art.download()
        
        # Makaleyi analiz et
        art.parse()
        art.nlp()
        
        title.config(state="normal") # kullanıcı tarafından düzenlenebilir hale getirilmesini sağlar.
        author.config(state="normal")
        publish_date.config(state="normal")
        summary.config(state="normal")
        sentiment.config(state="normal")

        title.delete("1.0", "end")
        title.insert("1.0", art.title)

        author.delete("1.0", "end")
        author.insert("1.0", ', '.join(art.authors))

        publish_date.delete("1.0", "end")
        pub_date = art.publish_date if art.publish_date else "Unknown"
        publish_date.insert("1.0", str(pub_date))

        summary.delete("1.0", "end")
        summary.insert("1.0", art.summary)

        analysis = TextBlob(art.text)
        sentiment.delete("1.0", "end")
        sentiment.insert("1.0", f'Polarity : {analysis.sentiment.polarity}, Sentiment : {"positive" if analysis.sentiment.polarity > 0 else "negative" if analysis.sentiment.polarity < 0 else "neutral"}')

        title.config(state="disabled")
        author.config(state="disabled")
        publish_date.config(state="disabled")
        summary.config(state="disabled")
        sentiment.config(state="disabled")

        print(analysis.sentiment)
        print(f'Sentiment: {"positive" if analysis.sentiment.polarity > 0 else "negative" if analysis.sentiment.polarity < 0 else "neutral"}')
    except Exception as e:
        print(f"Error: {e}")

#Tkinter kullanarak bir pencere oluşturur
root = tk.Tk()
root.title("News Summarizer")
root.geometry("1200x600")

tlabel = tk.Label(root, text="Title")
tlabel.pack()
#pack() metodu, widget'ı, içindeki diğer widget'larla birlikte düzenli bir şekilde pencere içinde yerleştirir

title = tk.Text(root, height=1, width=140)
title.config(state="disabled", bg="pink")
title.pack()

alabel = tk.Label(root, text="Author")
alabel.pack()

author = tk.Text(root, height=1, width=140)
author.config(state="disabled", bg="pink")
author.pack()

plabel = tk.Label(root, text="Publication Date")
plabel.pack()

publish_date = tk.Text(root, height=1, width=140)
publish_date.config(state="disabled", bg="pink")
publish_date.pack()

slabel = tk.Label(root, text="Summary")
slabel.pack()

summary = tk.Text(root, height=20, width=140)
summary.config(state="disabled", bg="pink")
summary.pack()

selabel = tk.Label(root, text="Sentiment Analysis")
selabel.pack()

sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state="disabled", bg="pink")
sentiment.pack()

ulabel = tk.Label(root, text="URL")
ulabel.pack()

utext = tk.Text(root, height=1, width=140)
utext.pack()

btn = tk.Button(root, text="Summarize", command=summarize)
btn.pack()

root.mainloop()
