import pandas as pd
import matplotlib.pyplot as plt

# მონაცემები
data = {
    'პროდუქტი': ['ვაშლი', 'ბანანი', 'ფორთოხალი'],
    'ფასი': [2.5, 1.8, 3.2]
}

df = pd.DataFrame(data)

# გრაფიკის აგება (სვეტოვანი დიაგრამა)
df.plot(x='პროდუქტი', y='ფასი', kind='bar', color='skyblue')

plt.title('ხილის ფასების დიაგრამა')
plt.ylabel('ფასი (ლარი)')
plt.show() # ეს ხაზი აუცილებელია ფანჯრის გამოსაჩენად