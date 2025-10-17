**Ziel:**  
Ein Modell erstellen, das E-Mails oder SMS automatisch in **Spam** und **Ham (nicht-Spam)** klassifiziert. Das Projekt vermittelt, wie Naive-Bayes-Klassifikation funktioniert und wie Wortwahrscheinlichkeiten für Entscheidungen genutzt werden.

**Datensatz**
Ich habe für das Training die Datensätze von Kaggle verwendet, die eine Gewichtung von 87 % Ham-Nachrichten und 12 % Spam-Nachrichten enthalten.
Unter diesem Link stammen meine Trainingsdaten: https://www.kaggle.com/datasets/venky73/spam-mails-dataset/data

**Genauigkeit**
F1: 0.98 -> Modell versteht alle Klasse gleich genau und mogelt nicht. 


**Frontend**

Ich habe am Anfang **Streamlit** verwendet, aber es ist nicht möglich, von außen neue Informationen einzureichen. Deswegen nutze ich lieber **Flask**.

----


**Die Ergebnisse**

Eine Vertrauenswürdige Nachricht:

![Ham Message](https://github.com/Juljano/Spamfilter-Naive-Bayes/raw/main/images/ham-message.png)








Eine Spam-Nachricht: 

![Spam Message](https://github.com/Juljano/Spamfilter-Naive-Bayes/raw/main/images/spam-message.png)
