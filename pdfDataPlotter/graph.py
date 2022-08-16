#Graph from pdf data by txddy-p
import textract
import matplotlib.pyplot as plt

text1 = textract.process("val.pdf")
text1 = text1.decode("utf-8")
text1 = text1.replace('\n','*')
text = text1.strip()

text = text.split('*')
ind = text.index('http://www.femm.info/wiki/download')
text = text[ind+1::]

B,H = [],[]
for i in text:
     q = text.count('B')
     w = text.count('')
     e = text.count('H')


while (q>0):
     a = text.remove('B')
     a = text.remove('H')     
     #a = text.remove('*')
     q-=1

while (w>0):
     a = text.remove('')
     w-=1

text[70] = text[70].strip() #removes white space


for i in text:
     a = float(i)
     if a < 10.0:
          B.append(a)
     else:
          H.append(a)

print("________________\n|     B|       H|")

x = "B,H"
for i in range(len(B)):
     b,h = str(B[i]).ljust(6,' '),str(H[i]).rjust(8,' ')
     x+=f"\n{B[i]},{H[i]}"
     print(f"|{b}|{h}|")
ind = H.index(56.0)
print(ind)
print((H[ind]))
i = ind+1
b , h = B[:i:], H[:i:]

with open('data.txt', 'w') as f:
    f.write(x)
plt.plot(h,b)
plt.xlabel('H')
plt.ylabel('B')
plt.title('B-H curve')
plt.show()