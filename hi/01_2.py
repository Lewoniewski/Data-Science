yatri_sankhya = int(input("कृपया यात्रियों की संख्या दर्ज करें: "))

if yatri_sankhya <= 35:
    print("यात्रा के लिए बस चुनें।")
elif yatri_sankhya <= 120:
    print("यात्रा के लिए ट्रेन चुनें।")
else:
    print("यात्रा के लिए हवाई जहाज चुनें।")
