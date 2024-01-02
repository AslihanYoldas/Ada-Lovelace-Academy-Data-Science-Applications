def my_function():
    print("Hello")

# bu modülü import ettiğinizde main çalışmıyor
# Böylece modülün içindeki import edildiğinde çalışmaması gereken kodlar çalışmayacaktır
# Kod akışı çalışmadan fonksiyonların import edilmesi sağlanır
# modüler yapılar kullanırken yardımcı olacaktır 
if __name__=="main":
    print('Not suppose to work')
    my_function()