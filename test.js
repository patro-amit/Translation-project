        console.log('🚀 JavaScript V2.0 Loading - Clickable schemes enabled');
        console.log('Timestamp:', new Date().toISOString());

        // ==================== UI LANGUAGE TRANSLATIONS ====================
        const uiTranslations = {
            'en': {
                languageName: 'English',
                navbar: {
                    title: '🌾 Farmer Portal | Scheme Translator'
                },
                hero: {
                    title: 'Government Scheme Translator',
                    subtitle: 'Government Farming Scheme Translator',
                    description1: 'Get clear details of government farming schemes in your own language.',
                    description2: 'Understand government farming schemes in your own language.',
                    description3: 'Translate English/Hindi scheme details into various Indian regional languages.'
                },
                schemes: {
                    header: 'Popular Government Schemes',
                    pmkisan: 'PM Kisan Samman Nidhi<br>₹6000/year direct benefit',
                    pmfby: 'Crop Insurance Scheme<br>Crop Insurance Scheme',
                    kcc: 'Kisan Credit Card<br>Easy Credit for Farmers',
                    info: 'Select scheme details above and translate to your language below'
                },
                form: {
                    header: 'Start Translation',
                    inputType: 'Choose Input Type:',
                    textInput: '✍️ Text Input',
                    imageInput: '🖼️ Image Upload - OCR',
                    audioInput: '🎤 Audio Upload - STT',
                    targetLanguage: 'Select Target Language:',
                    enterText: 'Enter English or Hindi Text:',
                    textPlaceholder: 'Type or paste scheme details, information, or any text here...',
                    tip: 'Tip: Copy scheme details from government websites and paste here for translation',
                    uploadFile: 'Upload File:',
                    translateButton: 'Translate Now'
                },
                loading: {
                    message: 'Processing, please wait...'
                },
                results: {
                    header: 'Translation Results',
                    originalText: 'Original Text',
                    translation: 'Translation',
                    listen: 'Listen'
                },
                activity: {
                    header: 'Activity Log',
                    noActivity: 'No recent translation activity logged.'
                },
                footer: {
                    tagline: '🌾 Serving Farmers with Dedication 🌾',
                    copyright: '© {{ current_year }} Farmer Scheme Translator Portal',
                    madewith: 'Made with care for Indian farmers and communities'
                }
            },
            'hi': {
                languageName: 'हिंदी',
                navbar: {
                    title: '🌾 किसान योजना अनुवादक | Farmer Portal'
                },
                hero: {
                    title: 'सरकारी योजना अनुवादक',
                    subtitle: 'सरकारी कृषि योजना अनुवादक',
                    description1: 'किसानों के लिए सरकारी योजनाओं को अपनी भाषा में समझें।',
                    description2: 'सरकारी कृषि योजनाओं को अपनी भाषा में समझें।',
                    description3: 'अंग्रेजी/हिंदी योजना विवरण को विभिन्न भारतीय क्षेत्रीय भाषाओं में अनुवाद करें।'
                },
                schemes: {
                    header: 'लोकप्रिय सरकारी योजनाएं',
                    pmkisan: 'प्रधानमंत्री किसान सम्मान निधि<br>₹6000/वर्ष प्रत्यक्ष लाभ',
                    pmfby: 'फसल बीमा योजना<br>फसल बीमा योजना',
                    kcc: 'किसान क्रेडिट कार्ड<br>किसानों के लिए आसान ऋण',
                    info: 'ऊपर योजना विवरण चुनें और नीचे अपनी भाषा में अनुवाद करें'
                },
                form: {
                    header: 'अनुवाद शुरू करें',
                    inputType: 'इनपुट प्रकार चुनें:',
                    textInput: '✍️ टेक्स्ट इनपुट',
                    imageInput: '🖼️ छवि अपलोड - OCR',
                    audioInput: '🎤 ऑडियो अपलोड - STT',
                    targetLanguage: 'लक्ष्य भाषा चुनें:',
                    enterText: 'अंग्रेजी या हिंदी टेक्स्ट दर्ज करें:',
                    textPlaceholder: 'यहाँ योजना विवरण, जानकारी या कोई टेक्स्ट टाइप या पेस्ट करें...',
                    tip: 'सुझाव: सरकारी वेबसाइटों से योजना विवरण कॉपी करें और अनुवाद के लिए यहाँ पेस्ट करें',
                    uploadFile: 'फ़ाइल अपलोड करें:',
                    translateButton: 'अनुवाद करें'
                },
                loading: {
                    message: 'प्रसंस्करण जारी है, कृपया प्रतीक्षा करें...'
                },
                results: {
                    header: 'अनुवाद परिणाम',
                    originalText: 'मूल पाठ',
                    translation: 'अनुवाद',
                    listen: 'सुनें'
                },
                activity: {
                    header: 'गतिविधि लॉग',
                    noActivity: 'अभी तक कोई अनुवाद गतिविधि नहीं।'
                },
                footer: {
                    tagline: '🌾 सेवा भाव से किसानों के लिए 🌾',
                    copyright: '© {{ current_year }} किसान योजना अनुवादक पोर्टल',
                    madewith: 'भारतीय किसानों और समुदायों के लिए सावधानी से बनाया गया'
                }
            },
            'bn': {
                languageName: 'বাংলা',
                navbar: {
                    title: '🌾 কৃষক পোর্টাল | স্কিম অনুবাদক'
                },
                hero: {
                    title: 'সরকারি স্কিম অনুবাদক',
                    subtitle: 'সরকারি কৃষি স্কিম অনুবাদক',
                    description1: 'আপনার নিজের ভাষায় সরকারি কৃষি স্কিম বুঝুন।',
                    description2: 'আপনার নিজের ভাষায় সরকারি কৃষি স্কিম বুঝুন।',
                    description3: 'ইংরেজি/হিন্দি স্কিম বিবরণ বিভিন্ন ভারতীয় আঞ্চলিক ভাষায় অনুবাদ করুন।'
                },
                schemes: {
                    header: 'জনপ্রিয় সরকারি স্কিম',
                    pmkisan: 'প্রধানমন্ত্রী কিষাণ সম্মান নিধি<br>₹6000/বছর সরাসরি সুবিধা',
                    pmfby: 'ফসল বীমা স্কিম<br>ফসলবীমা স্কিম',
                    kcc: 'কিষাণ ক্রেডিট কার্ড<br>কৃষকদের জন্য সহজ ঋণ',
                    info: 'উপরে স্কিম বিবরণ নির্বাচন করুন এবং নীচে আপনার ভাষায় অনুবাদ করুন'
                },
                form: {
                    header: 'অনুবাদ শুরু করুন',
                    inputType: 'ইনপুট টাইপ চয়ন করুন:',
                    textInput: '✍️ টেক্সট ইনপুট',
                    imageInput: '🖼️ ছবি আপলোড - OCR',
                    audioInput: '🎤 অডিও আপলোড - STT',
                    targetLanguage: 'লক্ষ্য ভাষা নির্বাচন করুন:',
                    enterText: 'ইংরেজি বা হিন্দি টেক্সট প্রবেশ করুন:',
                    textPlaceholder: 'এখানে স্কিম বিবরণ, তথ্য বা যেকোনো টেক্সট টাইপ বা পেস্ট করুন...',
                    tip: 'পরামর্শ: সরকারি ওয়েবসাইট থেকে স্কিম বিবরণ কপি করুন এবং অনুবাদের জন্য এখানে পেস্ট করুন',
                    uploadFile: 'ফাইল আপলোড করুন:',
                    translateButton: 'এখনই অনুবাদ করুন'
                },
                loading: {
                    message: 'প্রক্রিয়াকরণ, অনুগ্রহ করে অপেক্ষা করুন...'
                },
                results: {
                    header: 'অনুবাদ ফলাফল',
                    originalText: 'মূল টেক্সট',
                    translation: 'অনুবাদ',
                    listen: 'শুনুন'
                },
                activity: {
                    header: 'কার্যকলাপ লগ',
                    noActivity: 'এখনও কোন অনুবাদ কার্যকলাপ লগ করা হয়নি।'
                },
                footer: {
                    tagline: '🌾 নিষ্ঠার সাথে কৃষকদের সেবা করা 🌾',
                    copyright: '© {{ current_year }} কৃষক স্কিম অনুবাদক পোর্টাল',
                    madewith: 'ভারতীয় কৃষক এবং সম্প্রদায়ের জন্য যত্ন সহকারে তৈরি'
                }
            },
            'ta': {
                languageName: 'தமிழ்',
                navbar: {
                    title: '🌾 விவசாயி போர்ட்டல் | திட்ட மொழிபெயர்ப்பாளர்'
                },
                hero: {
                    title: 'அரசு திட்ட மொழிபெயர்ப்பாளர்',
                    subtitle: 'அரசு விவசாய திட்ட மொழிபெயர்ப்பாளர்',
                    description1: 'உங்கள் சொந்த மொழியில் அரசு விவசாய திட்டங்களை புரிந்து கொள்ளுங்கள்.',
                    description2: 'உங்கள் சொந்த மொழியில் அரசு விவசாய திட்டங்களை புரிந்து கொள்ளுங்கள்.',
                    description3: 'ஆங்கிலம்/இந்தி திட்ட விவரங்களை பல்வேறு இந்திய பிராந்திய மொழிகளாக மொழிபெயர்க்கவும்.'
                },
                schemes: {
                    header: 'பிரபலமான அரசு திட்டங்கள்',
                    pmkisan: 'பிரதம மந்திரி கிசான் சம்மான் நிதி<br>₹6000/ஆண்டு நேரடி நலன்',
                    pmfby: 'பயிர் காப்பீடு திட்டம்<br>பயிர் காப்பீடு திட்டம்',
                    kcc: 'கிசான் கிரெடிட் கார்டு<br>விவசாயிகளுக்கு எளிதான கடன்',
                    info: 'மேலே திட்ட விவரங்களைத் தேர்ந்தெடுத்து உங்கள் மொழியில் மொழிபெயர்க்கவும்'
                },
                form: {
                    header: 'மொழிபெயர்ப்பை தொடங்கவும்',
                    inputType: 'உள்ளீட்டு வகையைத் தேர்வு செய்யவும்:',
                    textInput: '✍️ உரை உள்ளீடு',
                    imageInput: '🖼️ படத்தை பதிவேற்றவும் - OCR',
                    audioInput: '🎤 ஆடியோ பதிவேற்றம் - STT',
                    targetLanguage: 'இலக்கு மொழியைத் தேர்ந்தெடுக்கவும்:',
                    enterText: 'ஆங்கிலம் அல்லது இந்தி உரையை உள்ளிடவும்:',
                    textPlaceholder: 'இங்கே திட்ட விவரங்கள், தகவல் அல்லது எந்த உரையையும் தட்டச்சு செய்யவும் அல்லது ஒட்டவும்...',
                    tip: 'குறிப்பு: அரசு இணையதளங்களிலிருந்து திட்ட விவரங்களை நகலெடுத்து மொழிபெயர்ப்பிற்காக இங்கே ஒட்டவும்',
                    uploadFile: 'கோப்பை பதிவேற்றவும்:',
                    translateButton: 'இப்போது மொழிபெயர்க்கவும்'
                },
                loading: {
                    message: 'செயலாக்கம், தயவுசெய்து காத்திருங்கள்...'
                },
                results: {
                    header: 'மொழிபெயர்ப்பு முடிவுகள்',
                    originalText: 'அசல் உரை',
                    translation: 'மொழிபெயர்ப்பு',
                    listen: 'கேளுங்கள்'
                },
                activity: {
                    header: 'செயல்பாடு பதிவு',
                    noActivity: 'சமீபத்திய மொழிபெயர்ப்பு செயல்பாடு எதுவும் பதிவு செய்யப்படவில்லை.'
                },
                footer: {
                    tagline: '🌾 விவசாயிகளுக்கு அர்ப்பணிப்புடன் சேவை செய்தல் 🌾',
                    copyright: '© {{ current_year }} விவசாயி திட்ட மொழிபெயர்ப்பாளர் போர்ட்டல்',
                    madewith: 'இந்திய விவசாயிகள் மற்றும் சமூகங்களுக்காக அக்கறையுடன் உருவாக்கப்பட்டது'
                }
            },
            'te': {
                languageName: 'తెలుగు',
                navbar: {
                    title: '🌾 రైతు పోర్టల్ | పథకం అనువాదకుడు'
                },
                hero: {
                    title: 'ప్రభుత్వ పథకం అనువాదకుడు',
                    subtitle: 'ప్రభుత్వ వ్యవసాయ పథకం అనువాదకుడు',
                    description1: 'మీ స్వంత భాషలో ప్రభుత్వ వ్యవసాయ పథకాలను అర్థం చేసుకోండి.',
                    description2: 'మీ స్వంత భాషలో ప్రభుత్వ వ్యవసాయ పథకాలను అర్థం చేసుకోండి.',
                    description3: 'ఆంగ్లం/హిందీ పథకం వివరాలను వివిధ భారతీయ ప్రాంతీయ భాషలలోకి అనువదించండి.'
                },
                schemes: {
                    header: 'ప్రముఖ ప్రభుత్వ పథకాలు',
                    pmkisan: 'ప్రధాన మంత్రి కిసాన్ సమ్మాన్ నిధి<br>₹6000/సంవత్సరం ప్రత్యక్ష ప్రయోజనం',
                    pmfby: 'పంట బీమా పథకం<br>పంట బీమా పథకం',
                    kcc: 'కిసాన్ క్రెడిట్ కార్డ్<br>రైతులకు సులభ రుణం',
                    info: 'పైన పథకం వివరాలను ఎంచుకోండి మరియు దిగువ మీ భాషలోకి అనువదించండి'
                },
                form: {
                    header: 'అనువాదాన్ని ప్రారంభించండి',
                    inputType: 'ఇన్‌పుట్ రకాన్ని ఎంచుకోండి:',
                    textInput: '✍️ టెక్స్ట్ ఇన్‌పుట్',
                    imageInput: '🖼️ చిత్రం అప్‌లోడ్ - OCR',
                    audioInput: '🎤 ఆడియో అప్‌లోడ్ - STT',
                    targetLanguage: 'లక్ష్య భాషను ఎంచుకోండి:',
                    enterText: 'ఆంగ్లం లేదా హిందీ టెక్స్ట్ నమోదు చేయండి:',
                    textPlaceholder: 'ఇక్కడ పథకం వివరాలు, సమాచారం లేదా ఏదైనా టెక్స్ట్ టైప్ చేయండి లేదా పేస్ట్ చేయండి...',
                    tip: 'చిట్కా: ప్రభుత్వ వెబ్‌సైట్‌ల నుండి పథకం వివరాలను కాపీ చేసి అనువాదం కోసం ఇక్కడ పేస్ట్ చేయండి',
                    uploadFile: 'ఫైల్ అప్‌లోడ్ చేయండి:',
                    translateButton: 'ఇప్పుడే అనువదించండి'
                },
                loading: {
                    message: 'ప్రాసెసింగ్, దయచేసి వేచి ఉండండి...'
                },
                results: {
                    header: 'అనువాద ఫలితాలు',
                    originalText: 'అసలు టెక్స్ట్',
                    translation: 'అనువాదం',
                    listen: 'వినండి'
                },
                activity: {
                    header: 'కార్యాచరణ లాగ్',
                    noActivity: 'ఇటీవలి అనువాద కార్యాచరణ ఏదీ లాగ్ చేయబడలేదు.'
                },
                footer: {
                    tagline: '🌾 అంకితభావంతో రైతులకు సేవ 🌾',
                    copyright: '© {{ current_year }} రైతు పథకం అనువాదకుడు పోర్టల్',
                    madewith: 'భారతీయ రైతులు మరియు సంఘాల కోసం శ్రద్ధతో రూపొందించబడింది'
                }
            },
            'mr': {
                languageName: 'मराठी',
                navbar: {
                    title: '🌾 शेतकरी पोर्टल | योजना अनुवादक'
                },
                hero: {
                    title: 'सरकारी योजना अनुवादक',
                    subtitle: 'सरकारी शेती योजना अनुवादक',
                    description1: 'तुमच्या स्वत:च्या भाषेत सरकारी शेती योजना समजून घ्या.',
                    description2: 'तुमच्या स्वत:च्या भाषेत सरकारी शेती योजना समजून घ्या.',
                    description3: 'इंग्रजी/हिंदी योजना तपशील विविध भारतीय प्रादेशिक भाषांमध्ये भाषांतरित करा.'
                },
                schemes: {
                    header: 'लोकप्रिय सरकारी योजना',
                    pmkisan: 'पंतप्रधान किसान सन्मान निधी<br>₹6000/वर्ष थेट लाभ',
                    pmfby: 'पीक विमा योजना<br>पीक विमा योजना',
                    kcc: 'किसान क्रेडिट कार्ड<br>शेतकऱ्यांसाठी सोपे कर्ज',
                    info: 'वर योजना तपशील निवडा आणि खाली तुमच्या भाषेत भाषांतर करा'
                },
                form: {
                    header: 'भाषांतर सुरू करा',
                    inputType: 'इनपुट प्रकार निवडा:',
                    textInput: '✍️ मजकूर इनपुट',
                    imageInput: '🖼️ प्रतिमा अपलोड - OCR',
                    audioInput: '🎤 ऑडिओ अपलोड - STT',
                    targetLanguage: 'लक्ष्य भाषा निवडा:',
                    enterText: 'इंग्रजी किंवा हिंदी मजकूर प्रविष्ट करा:',
                    textPlaceholder: 'येथे योजना तपशील, माहिती किंवा कोणताही मजकूर टाईप करा किंवा पेस्ट करा...',
                    tip: 'टीप: सरकारी वेबसाईट्सवरून योजना तपशील कॉपी करा आणि भाषांतरासाठी येथे पेस्ट करा',
                    uploadFile: 'फाईल अपलोड करा:',
                    translateButton: 'आता भाषांतर करा'
                },
                loading: {
                    message: 'प्रक्रिया सुरू आहे, कृपया प्रतीक्षा करा...'
                },
                results: {
                    header: 'भाषांतर परिणाम',
                    originalText: 'मूळ मजकूर',
                    translation: 'भाषांतर',
                    listen: 'ऐका'
                },
                activity: {
                    header: 'क्रियाकलाप लॉग',
                    noActivity: 'अजून कोणतीही भाषांतर क्रियाकलाप लॉग केली नाही.'
                },
                footer: {
                    tagline: '🌾 समर्पणाने शेतकऱ्यांची सेवा 🌾',
                    copyright: '© {{ current_year }} शेतकरी योजना अनुवादक पोर्टल',
                    madewith: 'भारतीय शेतकरी आणि समुदायांसाठी काळजीपूर्वक तयार केले'
                }
            },
            'gu': {
                languageName: 'ગુજરાતી',
                navbar: {
                    title: '🌾 ખેડૂત પોર્ટલ | યોજના અનુવાદક'
                },
                hero: {
                    title: 'સરકારી યોજના અનુવાદક',
                    subtitle: 'સરકારી ખેતી યોજના અનુવાદક',
                    description1: 'તમારી પોતાની ભાષામાં સરકારી ખેતી યોજનાઓ સમજો.',
                    description2: 'તમારી પોતાની ભાષામાં સરકારી ખેતી યોજનાઓ સમજો.',
                    description3: 'અંગ્રેજી/હિન્દી યોજના વિગતોને વિવિધ ભારતીય પ્રાદેશિક ભાષાઓમાં અનુવાદ કરો.'
                },
                schemes: {
                    header: 'લોકપ્રિય સરકારી યોજનાઓ',
                    pmkisan: 'પ્રધાનમંત્રી કિસાન સમ્માન નિધિ<br>₹6000/વર્ષ સીધો લાભ',
                    pmfby: 'પાક વીમા યોજના<br>પાક વીમા યોજના',
                    kcc: 'કિસાન ક્રેડિટ કાર્ડ<br>ખેડૂતો માટે સરળ ધિરાણ',
                    info: 'ઉપર યોજના વિગતો પસંદ કરો અને નીચે તમારી ભાષામાં અનુવાદ કરો'
                },
                form: {
                    header: 'અનુવાદ શરૂ કરો',
                    inputType: 'ઇનપુટ પ્રકાર પસંદ કરો:',
                    textInput: '✍️ ટેક્સ્ટ ઇનપુટ',
                    imageInput: '🖼️ છબી અપલોડ - OCR',
                    audioInput: '🎤 ઓડિયો અપલોડ - STT',
                    targetLanguage: 'લક્ષ્ય ભાષા પસંદ કરો:',
                    enterText: 'અંગ્રેજી અથવા હિન્દી ટેક્સ્ટ દાખલ કરો:',
                    textPlaceholder: 'અહીં યોજના વિગતો, માહિતી અથવા કોઈપણ ટેક્સ્ટ ટાઈપ કરો અથવા પેસ્ટ કરો...',
                    tip: 'ટિપ: સરકારી વેબસાઈટ્સમાંથી યોજના વિગતો કોપી કરો અને અનુવાદ માટે અહીં પેસ્ટ કરો',
                    uploadFile: 'ફાઈલ અપલોડ કરો:',
                    translateButton: 'હમણાં અનુવાદ કરો'
                },
                loading: {
                    message: 'પ્રક્રિયા ચાલુ છે, કૃપા કરીને રાહ જુઓ...'
                },
                results: {
                    header: 'અનુવાદ પરિણામો',
                    originalText: 'મૂળ ટેક્સ્ટ',
                    translation: 'અનુવાદ',
                    listen: 'સાંભળો'
                },
                activity: {
                    header: 'પ્રવૃત્તિ લોગ',
                    noActivity: 'હજુ સુધી કોઈ અનુવાદ પ્રવૃત્તિ લોગ થયેલ નથી.'
                },
                footer: {
                    tagline: '🌾 સમર્પણ સાથે ખેડૂતોની સેવા 🌾',
                    copyright: '© {{ current_year }} ખેડૂત યોજના અનુવાદક પોર્ટલ',
                    madewith: 'ભારતીય ખેડૂતો અને સમુદાયો માટે કાળજીપૂર્વક બનાવેલ'
                }
            },
            'kn': {
                languageName: 'ಕನ್ನಡ',
                navbar: {
                    title: '🌾 ರೈತ ಪೋರ್ಟಲ್ | ಯೋಜನೆ ಅನುವಾದಕ'
                },
                hero: {
                    title: 'ಸರ್ಕಾರಿ ಯೋಜನೆ ಅನುವಾದಕ',
                    subtitle: 'ಸರ್ಕಾರಿ ಕೃಷಿ ಯೋಜನೆ ಅನುವಾದಕ',
                    description1: 'ನಿಮ್ಮ ಸ್ವಂತ ಭಾಷೆಯಲ್ಲಿ ಸರ್ಕಾರಿ ಕೃಷಿ ಯೋಜನೆಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳಿ.',
                    description2: 'ನಿಮ್ಮ ಸ್ವಂತ ಭಾಷೆಯಲ್ಲಿ ಸರ್ಕಾರಿ ಕೃಷಿ ಯೋಜನೆಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳಿ.',
                    description3: 'ಇಂಗ್ಲಿಷ್/ಹಿಂದಿ ಯೋಜನೆ ವಿವರಗಳನ್ನು ವಿವಿಧ ಭಾರತೀಯ ಪ್ರಾದೇಶಿಕ ಭಾಷೆಗಳಿಗೆ ಭಾಷಾಂತರಿಸಿ.'
                },
                schemes: {
                    header: 'ಜನಪ್ರಿಯ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು',
                    pmkisan: 'ಪ್ರಧಾನ ಮಂತ್ರಿ ಕಿಸಾನ್ ಸಮ್ಮಾನ್ ನಿಧಿ<br>₹6000/ವರ್ಷ ನೇರ ಲಾಭ',
                    pmfby: 'ಬೆಳೆ ವಿಮಾ ಯೋಜನೆ<br>ಬೆಳೆ ವಿಮಾ ಯೋಜನೆ',
                    kcc: 'ಕಿಸಾನ್ ಕ್ರೆಡಿಟ್ ಕಾರ್ಡ್<br>ರೈತರಿಗೆ ಸುಲಭ ಸಾಲ',
                    info: 'ಮೇಲೆ ಯೋಜನೆ ವಿವರಗಳನ್ನು ಆಯ್ಕೆ ಮಾಡಿ ಮತ್ತು ಕೆಳಗೆ ನಿಮ್ಮ ಭಾಷೆಗೆ ಭಾಷಾಂತರಿಸಿ'
                },
                form: {
                    header: 'ಭಾಷಾಂತರ ಪ್ರಾರಂಭಿಸಿ',
                    inputType: 'ಇನ್‌ಪುಟ್ ಪ್ರಕಾರವನ್ನು ಆಯ್ಕೆ ಮಾಡಿ:',
                    textInput: '✍️ ಪಠ್ಯ ಇನ್‌ಪುಟ್',
                    imageInput: '🖼️ ಚಿತ್ರ ಅಪ್‌ಲೋಡ್ - OCR',
                    audioInput: '🎤 ಆಡಿಯೋ ಅಪ್‌ಲೋಡ್ - STT',
                    targetLanguage: 'ಗುರಿ ಭಾಷೆಯನ್ನು ಆರಿಸಿ:',
                    enterText: 'ಇಂಗ್ಲಿಷ್ ಅಥವಾ ಹಿಂದಿ ಪಠ್ಯವನ್ನು ನಮೂದಿಸಿ:',
                    textPlaceholder: 'ಇಲ್ಲಿ ಯೋಜನೆ ವಿವರಗಳು, ಮಾಹಿತಿ ಅಥವಾ ಯಾವುದೇ ಪಠ್ಯವನ್ನು ಟೈಪ್ ಮಾಡಿ ಅಥವಾ ಅಂಟಿಸಿ...',
                    tip: 'ಸಲಹೆ: ಸರ್ಕಾರಿ ವೆಬ್‌ಸೈಟ್‌ಗಳಿಂದ ಯೋಜನೆ ವಿವರಗಳನ್ನು ನಕಲಿಸಿ ಮತ್ತು ಭಾಷಾಂತರಕ್ಕಾಗಿ ಇಲ್ಲಿ ಅಂಟಿಸಿ',
                    uploadFile: 'ಫೈಲ್ ಅಪ್‌ಲೋಡ್ ಮಾಡಿ:',
                    translateButton: 'ಈಗ ಭಾಷಾಂತರಿಸಿ'
                },
                loading: {
                    message: 'ಪ್ರಕ್ರಿಯೆಯಲ್ಲಿದೆ, ದಯವಿಟ್ಟು ನಿರೀಕ್ಷಿಸಿ...'
                },
                results: {
                    header: 'ಭಾಷಾಂತರ ಫಲಿತಾಂಶಗಳು',
                    originalText: 'ಮೂಲ ಪಠ್ಯ',
                    translation: 'ಭಾಷಾಂತರ',
                    listen: 'ಕೇಳಿ'
                },
                activity: {
                    header: 'ಚಟುವಟಿಕೆ ಲಾಗ್',
                    noActivity: 'ಇತ್ತೀಚಿನ ಭಾಷಾಂತರ ಚಟುವಟಿಕೆ ಲಾಗ್ ಮಾಡಲಾಗಿಲ್ಲ.'
                },
                footer: {
                    tagline: '🌾 ಸಮರ್ಪಣೆಯೊಂದಿಗೆ ರೈತರಿಗೆ ಸೇವೆ 🌾',
                    copyright: '© {{ current_year }} ರೈತ ಯೋಜನೆ ಅನುವಾದಕ ಪೋರ್ಟಲ್',
                    madewith: 'ಭಾರತೀಯ ರೈತರು ಮತ್ತು ಸಮುದಾಯಗಳಿಗಾಗಿ ಕಾಳಜಿಯೊಂದಿಗೆ ರಚಿಸಲಾಗಿದೆ'
                }
            },
            'ml': {
                languageName: 'മലയാളം',
                navbar: {
                    title: '🌾 കർഷക പോർട്ടൽ | പദ്ധതി വിവർത്തകൻ'
                },
                hero: {
                    title: 'സർക്കാർ പദ്ധതി വിവർത്തകൻ',
                    subtitle: 'സർക്കാർ കൃഷി പദ്ധതി വിവർത്തകൻ',
                    description1: 'നിങ്ങളുടെ സ്വന്തം ഭാഷയിൽ സർക്കാർ കൃഷി പദ്ധതികൾ മനസ്സിലാക്കുക.',
                    description2: 'നിങ്ങളുടെ സ്വന്തം ഭാഷയിൽ സർക്കാർ കൃഷി പദ്ധതികൾ മനസ്സിലാക്കുക.',
                    description3: 'ഇംഗ്ലീഷ്/ഹിന്ദി പദ്ധതി വിശദാംശങ്ങൾ വിവിധ ഇന്ത്യൻ പ്രാദേശിക ഭാഷകളിലേക്ക് വിവർത്തനം ചെയ്യുക.'
                },
                schemes: {
                    header: 'ജനപ്രിയ സർക്കാർ പദ്ധതികൾ',
                    pmkisan: 'പ്രധാനമന്ത്രി കിസാൻ സമ്മാൻ നിധി<br>₹6000/വർഷം നേരിട്ടുള്ള ആനുകൂല്യം',
                    pmfby: 'വിള ഇൻഷുറൻസ് പദ്ധതി<br>വിള ഇൻഷുറൻസ് പദ്ധതി',
                    kcc: 'കിസാൻ ക്രെഡിറ്റ് കാർഡ്<br>കർഷകർക്ക് എളുപ്പമുള്ള വായ്പ',
                    info: 'മുകളിൽ പദ്ധതി വിശദാംശങ്ങൾ തിരഞ്ഞെടുക്കുകയും താഴെ നിങ്ങളുടെ ഭാഷയിലേക്ക് വിവർത്തനം ചെയ്യുകയും ചെയ്യുക'
                },
                form: {
                    header: 'വിവർത്തനം ആരംഭിക്കുക',
                    inputType: 'ഇൻപുട്ട് തരം തിരഞ്ഞെടുക്കുക:',
                    textInput: '✍️ ടെക്സ്റ്റ് ഇൻപുട്ട്',
                    imageInput: '🖼️ ചിത്രം അപ്‌ലോഡ് - OCR',
                    audioInput: '🎤 ഓഡിയോ അപ്‌ലോഡ് - STT',
                    targetLanguage: 'ലക്ഷ്യ ഭാഷ തിരഞ്ഞെടുക്കുക:',
                    enterText: 'ഇംഗ്ലീഷ് അല്ലെങ്കിൽ ഹിന്ദി ടെക്സ്റ്റ് നൽകുക:',
                    textPlaceholder: 'ഇവിടെ പദ്ധതി വിശദാംശങ്ങൾ, വിവരങ്ങൾ അല്ലെങ്കിൽ ഏതെങ്കിലും ടെക്സ്റ്റ് ടൈപ്പ് ചെയ്യുക അല്ലെങ്കിൽ ഒട്ടിക്കുക...',
                    tip: 'സൂചന: സർക്കാർ വെബ്‌സൈറ്റുകളിൽ നിന്ന് പദ്ധതി വിശദാംശങ്ങൾ പകർത്തി വിവർത്തനത്തിനായി ഇവിടെ ഒട്ടിക്കുക',
                    uploadFile: 'ഫയൽ അപ്‌ലോഡ് ചെയ്യുക:',
                    translateButton: 'ഇപ്പോൾ വിവർത്തനം ചെയ്യുക'
                },
                loading: {
                    message: 'പ്രോസസ്സിംഗ്, ദയവായി കാത്തിരിക്കുക...'
                },
                results: {
                    header: 'വിവർത്തന ഫലങ്ങൾ',
                    originalText: 'യഥാർത്ഥ ടെക്സ്റ്റ്',
                    translation: 'വിവർത്തനം',
                    listen: 'കേൾക്കുക'
                },
                activity: {
                    header: 'പ്രവർത്തന ലോഗ്',
                    noActivity: 'സമീപകാല വിവർത്തന പ്രവർത്തനം ലോഗ് ചെയ്തിട്ടില്ല.'
                },
                footer: {
                    tagline: '🌾 സമർപ്പണത്തോടെ കർഷകർക്ക് സേവനം 🌾',
                    copyright: '© {{ current_year }} കർഷക പദ്ധതി വിവർത്തക പോർട്ടൽ',
                    madewith: 'ഇന്ത്യൻ കർഷകർക്കും സമുദായങ്ങൾക്കും വേണ്ടി ശ്രദ്ധയോടെ നിർമ്മിച്ചത്'
                }
            },
            'pa': {
                languageName: 'ਪੰਜਾਬੀ',
                navbar: {
                    title: '🌾 ਕਿਸਾਨ ਪੋਰਟਲ | ਸਕੀਮ ਅਨੁਵਾਦਕ'
                },
                hero: {
                    title: 'ਸਰਕਾਰੀ ਸਕੀਮ ਅਨੁਵਾਦਕ',
                    subtitle: 'ਸਰਕਾਰੀ ਖੇਤੀਬਾੜੀ ਸਕੀਮ ਅਨੁਵਾਦਕ',
                    description1: 'ਆਪਣੀ ਭਾਸ਼ਾ ਵਿੱਚ ਸਰਕਾਰੀ ਖੇਤੀਬਾੜੀ ਸਕੀਮਾਂ ਨੂੰ ਸਮਝੋ।',
                    description2: 'ਆਪਣੀ ਭਾਸ਼ਾ ਵਿੱਚ ਸਰਕਾਰੀ ਖੇਤੀਬਾੜੀ ਸਕੀਮਾਂ ਨੂੰ ਸਮਝੋ।',
                    description3: 'ਅੰਗਰੇਜ਼ੀ/ਹਿੰਦੀ ਸਕੀਮ ਵੇਰਵੇ ਨੂੰ ਵੱਖ-ਵੱਖ ਭਾਰਤੀ ਖੇਤਰੀ ਭਾਸ਼ਾਵਾਂ ਵਿੱਚ ਅਨੁਵਾਦ ਕਰੋ।'
                },
                schemes: {
                    header: 'ਪ੍ਰਸਿੱਧ ਸਰਕਾਰੀ ਸਕੀਮਾਂ',
                    pmkisan: 'ਪ੍ਰਧਾਨ ਮੰਤਰੀ ਕਿਸਾਨ ਸਮਾਨ ਨਿਧੀ<br>₹6000/ਸਾਲ ਸਿੱਧਾ ਲਾਭ',
                    pmfby: 'ਫਸਲ ਬੀਮਾ ਸਕੀਮ<br>ਫਸਲ ਬੀਮਾ ਸਕੀਮ',
                    kcc: 'ਕਿਸਾਨ ਕ੍ਰੈਡਿਟ ਕਾਰਡ<br>ਕਿਸਾਨਾਂ ਲਈ ਆਸਾਨ ਕਰਜ਼ਾ',
                    info: 'ਉੱਪਰ ਸਕੀਮ ਵੇਰਵੇ ਚੁਣੋ ਅਤੇ ਹੇਠਾਂ ਆਪਣੀ ਭਾਸ਼ਾ ਵਿੱਚ ਅਨੁਵਾਦ ਕਰੋ'
                },
                form: {
                    header: 'ਅਨੁਵਾਦ ਸ਼ੁਰੂ ਕਰੋ',
                    inputType: 'ਇਨਪੁੱਟ ਕਿਸਮ ਚੁਣੋ:',
                    textInput: '✍️ ਟੈਕਸਟ ਇਨਪੁੱਟ',
                    imageInput: '🖼️ ਚਿੱਤਰ ਅੱਪਲੋਡ - OCR',
                    audioInput: '🎤 ਆਡੀਓ ਅੱਪਲੋਡ - STT',
                    targetLanguage: 'ਟੀਚਾ ਭਾਸ਼ਾ ਚੁਣੋ:',
                    enterText: 'ਅੰਗਰੇਜ਼ੀ ਜਾਂ ਹਿੰਦੀ ਟੈਕਸਟ ਦਾਖਲ ਕਰੋ:',
                    textPlaceholder: 'ਇੱਥੇ ਸਕੀਮ ਵੇਰਵੇ, ਜਾਣਕਾਰੀ ਜਾਂ ਕੋਈ ਟੈਕਸਟ ਟਾਈਪ ਕਰੋ ਜਾਂ ਪੇਸਟ ਕਰੋ...',
                    tip: 'ਸੁਝਾਅ: ਸਰਕਾਰੀ ਵੈਬਸਾਈਟਾਂ ਤੋਂ ਸਕੀਮ ਵੇਰਵੇ ਕਾਪੀ ਕਰੋ ਅਤੇ ਅਨੁਵਾਦ ਲਈ ਇੱਥੇ ਪੇਸਟ ਕਰੋ',
                    uploadFile: 'ਫਾਈਲ ਅੱਪਲੋਡ ਕਰੋ:',
                    translateButton: 'ਹੁਣੇ ਅਨੁਵਾਦ ਕਰੋ'
                },
                loading: {
                    message: 'ਪ੍ਰਕਿਰਿਆ ਚੱਲ ਰਹੀ ਹੈ, ਕਿਰਪਾ ਕਰਕੇ ਉਡੀਕ ਕਰੋ...'
                },
                results: {
                    header: 'ਅਨੁਵਾਦ ਨਤੀਜੇ',
                    originalText: 'ਅਸਲੀ ਟੈਕਸਟ',
                    translation: 'ਅਨੁਵਾਦ',
                    listen: 'ਸੁਣੋ'
                },
                activity: {
                    header: 'ਗਤੀਵਿਧੀ ਲੌਗ',
                    noActivity: 'ਹਾਲੀਆ ਅਨੁਵਾਦ ਗਤੀਵਿਧੀ ਲੌਗ ਨਹੀਂ ਕੀਤੀ ਗਈ।'
                },
                footer: {
                    tagline: '🌾 ਸਮਰਪਣ ਨਾਲ ਕਿਸਾਨਾਂ ਦੀ ਸੇਵਾ 🌾',
                    copyright: '© {{ current_year }} ਕਿਸਾਨ ਸਕੀਮ ਅਨੁਵਾਦਕ ਪੋਰਟਲ',
                    madewith: 'ਭਾਰਤੀ ਕਿਸਾਨਾਂ ਅਤੇ ਭਾਈਚਾਰਿਆਂ ਲਈ ਸਾਵਧਾਨੀ ਨਾਲ ਬਣਾਇਆ ਗਿਆ'
                }
            },
            'or': {
                languageName: 'ଓଡ଼ିଆ',
                navbar: {
                    title: '🌾 କୃଷକ ପୋର୍ଟାଲ | ଯୋଜନା ଅନୁବାଦକ'
                },
                hero: {
                    title: 'ସରକାରୀ ଯୋଜନା ଅନୁବାଦକ',
                    subtitle: 'ସରକାରୀ କୃଷି ଯୋଜନା ଅନୁବାଦକ',
                    description1: 'ଆପଣଙ୍କ ନିଜ ଭାଷାରେ ସରକାରୀ କୃଷି ଯୋଜନା ବୁଝନ୍ତୁ।',
                    description2: 'ଆପଣଙ୍କ ନିଜ ଭାଷାରେ ସରକାରୀ କୃଷି ଯୋଜନା ବୁଝନ୍ତୁ।',
                    description3: 'ଇଂରାଜୀ/ହିନ୍ଦୀ ଯୋଜନା ବିବରଣୀକୁ ବିଭିନ୍ନ ଭାରତୀୟ ଆଞ୍ଚଳିକ ଭାଷାରେ ଅନୁବାଦ କରନ୍ତୁ।'
                },
                schemes: {
                    header: 'ଲୋକପ୍ରିୟ ସରକାରୀ ଯୋଜନା',
                    pmkisan: 'ପ୍ରଧାନମନ୍ତ୍ରୀ କିସାନ ସମ୍ମାନ ନିଧି<br>₹6000/ବର୍ଷ ସିଧାସଳଖ ଲାଭ',
                    pmfby: 'ଫସଲ ବୀମା ଯୋଜନା<br>ଫସଲ ବୀମା ଯୋଜନା',
                    kcc: 'କିସାନ କ୍ରେଡିଟ କାର୍ଡ<br>କୃଷକଙ୍କ ପାଇଁ ସହଜ ଋଣ',
                    info: 'ଉପରେ ଯୋଜନା ବିବରଣୀ ଚୟନ କରନ୍ତୁ ଏବଂ ତଳେ ଆପଣଙ୍କ ଭାଷାରେ ଅନୁବାଦ କରନ୍ତୁ'
                },
                form: {
                    header: 'ଅନୁବାଦ ଆରମ୍ଭ କରନ୍ତୁ',
                    inputType: 'ଇନପୁଟ ପ୍ରକାର ଚୟନ କରନ୍ତୁ:',
                    textInput: '✍️ ଟେକ୍ସଟ ଇନପୁଟ',
                    imageInput: '🖼️ ଚିତ୍ର ଅପଲୋଡ - OCR',
                    audioInput: '🎤 ଅଡିଓ ଅପଲୋଡ - STT',
                    targetLanguage: 'ଲକ୍ଷ୍ୟ ଭାଷା ଚୟନ କରନ୍ତୁ:',
                    enterText: 'ଇଂରାଜୀ କିମ୍ବା ହିନ୍ଦୀ ଟେକ୍ସଟ ପ୍ରବେଶ କରନ୍ତୁ:',
                    textPlaceholder: 'ଏଠାରେ ଯୋଜନା ବିବରଣୀ, ସୂଚନା କିମ୍ବା ଯେକୌଣସି ଟେକ୍ସଟ ଟାଇପ କରନ୍ତୁ କିମ୍ବା ପେଷ୍ଟ କରନ୍ତୁ...',
                    tip: 'ସୂଚନା: ସରକାରୀ ୱେବସାଇଟରୁ ଯୋଜନା ବିବରଣୀ କପି କରନ୍ତୁ ଏବଂ ଅନୁବାଦ ପାଇଁ ଏଠାରେ ପେଷ୍ଟ କରନ୍ତୁ',
                    uploadFile: 'ଫାଇଲ ଅପଲୋଡ କରନ୍ତୁ:',
                    translateButton: 'ବର୍ତ୍ତମାନ ଅନୁବାଦ କରନ୍ତୁ'
                },
                loading: {
                    message: 'ପ୍ରକ୍ରିୟାକରଣ, ଦୟାକରି ଅପେକ୍ଷା କରନ୍ତୁ...'
                },
                results: {
                    header: 'ଅନୁବାଦ ଫଳାଫଳ',
                    originalText: 'ମୂଳ ଟେକ୍ସଟ',
                    translation: 'ଅନୁବାଦ',
                    listen: 'ଶୁଣନ୍ତୁ'
                },
                activity: {
                    header: 'କାର୍ଯ୍ୟକଳାପ ଲଗ',
                    noActivity: 'ସମ୍ପ୍ରତି କୌଣସି ଅନୁବାଦ କାର୍ଯ୍ୟକଳାପ ଲଗ ହୋଇନାହିଁ।'
                },
                footer: {
                    tagline: '🌾 ସମର୍ପଣ ସହିତ କୃଷକଙ୍କ ସେବା 🌾',
                    copyright: '© {{ current_year }} କୃଷକ ଯୋଜନା ଅନୁବାଦକ ପୋର୍ଟାଲ',
                    madewith: 'ଭାରତୀୟ କୃଷକ ଏବଂ ସମ୍ପ୍ରଦାୟଙ୍କ ପାଇଁ ଯତ୍ନ ସହିତ ନିର୍ମିତ'
                }
            }
        };

        // ==================== LANGUAGE SWITCHER FUNCTION ====================
        function changeUILanguage(langCode) {
            const translations = uiTranslations[langCode];
            if (!translations) {
                console.error('Translation not found for language:', langCode);
                return;
            }

            // Update all elements with data-i18n attribute
            document.querySelectorAll('[data-i18n]').forEach(element => {
                const keys = element.getAttribute('data-i18n').split('.');
                let translation = translations;

                for (const key of keys) {
                    if (translation[key]) {
                        translation = translation[key];
                    } else {
                        console.warn('Translation key not found:', element.getAttribute('data-i18n'));
                        return;
                    }
                }

                element.innerHTML = translation;
            });

            // Update placeholders if they have data-i18n-placeholder attribute
            document.querySelectorAll('[data-i18n-placeholder]').forEach(element => {
                const keys = element.getAttribute('data-i18n-placeholder').split('.');
                let translation = translations;

                for (const key of keys) {
                    if (translation[key]) {
                        translation = translation[key];
                    } else {
                        return;
                    }
                }

                element.setAttribute('placeholder', translation);
            });

            // Update the language selector button
            document.getElementById('currentLanguageName').textContent = translations.languageName;

            // Store preference in localStorage (both keys for compatibility)
            localStorage.setItem('preferredUILanguage', langCode);
            localStorage.setItem('uiLanguage', langCode);

            // Update history labels when language changes
            translateHistoryLabels();

            // Clear scheme translation cache when language changes
            allSchemesTranslated = {};

            console.log('UI language changed to:', translations.languageName);
        }

        // Load saved language preference on page load
        document.addEventListener('DOMContentLoaded', function () {
            const savedLang = localStorage.getItem('preferredUILanguage');
            if (savedLang && uiTranslations[savedLang]) {
                changeUILanguage(savedLang);
            }
        });

        // ==================== EXISTING JAVASCRIPT ====================
        // Global skip interval, default to 5 seconds
        window.ttsSkipInterval = 5;

        function toggleInputFields() {
            const inputType = document.getElementById('input_type').value;
            const textDiv = document.getElementById('text_input_div');
            const fileDiv = document.getElementById('file_input_div');
            const fileHelp = document.getElementById('fileHelp');
            const fileInput = document.getElementById('file');

            textDiv.classList.add('file-input-hidden');
            fileDiv.classList.add('file-input-hidden');

            if (inputType === 'text') {
                textDiv.classList.remove('file-input-hidden');
                fileInput.value = '';
                fileInput.removeAttribute('accept');
                fileHelp.textContent = '';
            } else {
                fileDiv.classList.remove('file-input-hidden');
                document.getElementById('text_input').value = '';
                if (inputType === 'image') {
                    fileInput.setAttribute('accept', 'image/png, image/jpeg, image/jpg, image/gif, image/bmp, image/webp');
                    fileHelp.textContent = 'Allowed image types: PNG, JPG, JPEG, GIF, BMP, WEBP (Max 16MB)';
                } else { // audio
                    fileInput.setAttribute('accept', 'audio/mp3, audio/wav, audio/ogg, audio/flac, audio/m4a');
                    fileHelp.textContent = 'Allowed audio types: MP3, WAV, OGG, FLAC, M4A (Max 16MB)';
                }
            }
        }

        function setSkipInterval(seconds, playerContext) {
            window.ttsSkipInterval = parseInt(seconds, 10);
            document.querySelectorAll('.skip-interval-label-adjacent').forEach(label => {
                label.textContent = window.ttsSkipInterval;
            });
            console.log(`Skip interval set to: ${window.ttsSkipInterval}s for context: ${playerContext}`);
        }


        function skipAudio(audioPlayerId, seconds) {
            const audioPlayer = document.getElementById(audioPlayerId);
            if (audioPlayer && audioPlayer.src && (audioPlayer.duration > 0 && !audioPlayer.paused || audioPlayer.currentTime > 0)) {
                const newTime = audioPlayer.currentTime + seconds;
                audioPlayer.currentTime = Math.max(0, Math.min(audioPlayer.duration, newTime));
                console.log(`Skipped audio for ${audioPlayerId} by ${seconds}s. New time: ${audioPlayer.currentTime}`);
            } else {
                console.log(`Cannot skip audio for ${audioPlayerId}: Audio not loaded/playing or player not found.`);
            }
        }


        function playTTSGeneric(text, lang, audioPlayerId, listenButtonId, customControlsWrapperId, textContainerId = null) {
            console.log(`--- playTTSGeneric CALLED for ${audioPlayerId} ---`);
            const audioPlayer = document.getElementById(audioPlayerId);
            const listenButton = document.getElementById(listenButtonId);
            const customControlsWrapper = document.getElementById(customControlsWrapperId);

            if (text === null || typeof text === 'undefined' || (typeof text === 'string' && text.trim() === "")) {
                console.error(`TTS Error (${audioPlayerId}): Text is null, undefined, or empty string.`);
                alert("Cannot play: No valid text provided.");
                return;
            }
            if (typeof lang !== 'string' || lang.trim() === "") { console.error(`TTS Error (${audioPlayerId}): Lang invalid.`); alert("Cannot play: No lang."); return; }
            if (!audioPlayer) { console.error(`TTS Error (${audioPlayerId}): Audio player not found.`); alert("Player error."); return; }
            if (!customControlsWrapper) { console.error(`TTS Error (${audioPlayerId}): Controls wrapper not found.`); alert("Controls error."); return; }

            if (listenButton) {
                listenButton.disabled = true;
                listenButton.innerHTML = '<span class="spinner-border spinner-border-sm"></span> Loading...';
            }
            console.log(`Fetching TTS for ${audioPlayerId}: Text='${text.substring(0, 50)}', Lang='${lang}'`);

            fetch("{{ url_for('tts_route') }}", { method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: new URLSearchParams({ 'text': text, 'lang': lang }) })
                .then(response => {
                    console.log(`Fetch Status (${audioPlayerId}):`, response.status);
                    if (!response.ok) { return response.text().then(errTxt => { throw new Error(`TTS fail: ${response.statusText}. Server: ${errTxt}`); }); }
                    return response.blob();
                })
                .then(blob => {
                    console.log(`Blob (${audioPlayerId}):`, blob.type, blob.size);
                    if (blob.size === 0 || !blob.type.startsWith('audio/')) { throw new Error("Invalid audio data."); }
                    const audioUrl = URL.createObjectURL(blob);
                    audioPlayer.src = audioUrl;
                    customControlsWrapper.classList.remove('d-none');
                    if (listenButton) listenButton.classList.add('d-none');

                    // Setup word highlighting if textContainerId is provided
                    if (textContainerId) {
                        setupWordHighlighting(audioPlayer, textContainerId, text);
                    }

                    audioPlayer.play().catch(e => { console.error(`play() error (${audioPlayerId}):`, e); alert("Error playing: " + e.message); });
                    audioPlayer.onended = () => {
                        console.log(`Audio ended (${audioPlayerId}), revoking URL.`);
                        URL.revokeObjectURL(audioUrl);
                        customControlsWrapper.classList.add('d-none');
                        if (listenButton) listenButton.classList.remove('d-none');
                        // Clear highlighting when audio ends
                        if (textContainerId) {
                            clearWordHighlighting(textContainerId);
                        }
                    };
                })
                .catch(error => {
                    console.error(`TTS Error (${audioPlayerId}):`, error);
                    alert(`TTS failed for ${audioPlayerId}: ${error.message}`);
                    customControlsWrapper.classList.add('d-none');
                    if (listenButton) listenButton.classList.remove('d-none');
                })
                .finally(() => {
                    if (listenButton) {
                        listenButton.disabled = false;
                        listenButton.innerHTML = '<i class="bi bi-volume-up"></i> Listen';
                    }
                });
        }

        function playTTSMain() {
            const text = document.getElementById('ttsTextMain').value;
            const lang = document.getElementById('ttsLangMain').value;
            playTTSGeneric(text, lang, 'ttsAudioMain', 'ttsListenBtnMain', 'customAudioControlsWrapperMain', 'mainTranslationText');
        }

        function playTTSLogEntry(loopIndex) {
            const text = document.getElementById(`ttsTextLog${loopIndex}`).value;
            const lang = document.getElementById(`ttsLangLog${loopIndex}`).value;
            playTTSGeneric(text, lang, `ttsAudioLog${loopIndex}`, `ttsListenBtnLog${loopIndex}`, `customAudioControlsWrapperLog${loopIndex}`, `logTranslationTextContent${loopIndex}`);
        }


        // Word-by-word highlighting functionality
        function setupWordHighlighting(audioPlayer, textContainerId, text) {
            const textContainer = document.getElementById(textContainerId);
            if (!textContainer) return;

            // Split text into words while preserving spaces and punctuation
            const words = text.split(/\s+/).filter(w => w.length > 0);

            // Calculate timing for each word based on its length
            // gTTS speaks at approximately 150-180 words per minute (average 165)
            const baseCharsPerSecond = 12; // Approximate speaking rate
            let cumulativeTime = 0;
            const wordTimings = words.map(word => {
                // Add slight pause for punctuation
                const hasPunctuation = /[.!?,;:]$/.test(word);
                const wordDuration = (word.length / baseCharsPerSecond) + (hasPunctuation ? 0.3 : 0);
                const startTime = cumulativeTime;
                cumulativeTime += wordDuration;
                return {
                    word: word,
                    startTime: startTime,
                    endTime: cumulativeTime
                };
            });

            // Wrap each word in a span for individual highlighting
            textContainer.innerHTML = words.map((word, index) =>
                `<span class="tts-word" data-word-index="${index}">${word}</span>`
            ).join(' ');

            const wordSpans = textContainer.querySelectorAll('.tts-word');
            let animationFrameId = null;

            // Function to update highlight based on current audio time
            const updateHighlight = () => {
                if (audioPlayer.paused || audioPlayer.ended) {
                    return;
                }

                const currentTime = audioPlayer.currentTime;
                const totalDuration = audioPlayer.duration;

                // Scale the theoretical timings to match actual audio duration
                const timeScale = totalDuration / cumulativeTime;

                // Remove all highlights first
                wordSpans.forEach(span => span.classList.remove('tts-word-active'));

                // Find and highlight the current word
                for (let i = 0; i < wordTimings.length; i++) {
                    const scaledStart = wordTimings[i].startTime * timeScale;
                    const scaledEnd = wordTimings[i].endTime * timeScale;

                    if (currentTime >= scaledStart && currentTime < scaledEnd) {
                        wordSpans[i].classList.add('tts-word-active');

                        // Scroll to keep highlighted word visible
                        wordSpans[i].scrollIntoView({
                            behavior: 'smooth',
                            block: 'nearest',
                            inline: 'nearest'
                        });
                        break;
                    }
                }

                // Continue updating while playing
                animationFrameId = requestAnimationFrame(updateHighlight);
            };

            // Start highlighting when audio plays
            const startHighlighting = () => {
                if (animationFrameId) {
                    cancelAnimationFrame(animationFrameId);
                }
                updateHighlight();
            };

            // Stop highlighting
            const stopHighlighting = () => {
                if (animationFrameId) {
                    cancelAnimationFrame(animationFrameId);
                    animationFrameId = null;
                }
            };

            audioPlayer.addEventListener('play', startHighlighting);
            audioPlayer.addEventListener('playing', startHighlighting);
            audioPlayer.addEventListener('pause', stopHighlighting);
            audioPlayer.addEventListener('ended', () => {
                stopHighlighting();
                // Remove all highlights when ended
                wordSpans.forEach(span => span.classList.remove('tts-word-active'));
            });
            audioPlayer.addEventListener('seeked', () => {
                if (!audioPlayer.paused) {
                    updateHighlight();
                }
            });
        }

        function clearWordHighlighting(textContainerId) {
            const textContainer = document.getElementById(textContainerId);
            if (!textContainer) return;

            // Remove all highlighting classes
            const wordSpans = textContainer.querySelectorAll('.tts-word');
            wordSpans.forEach(span => span.classList.remove('tts-word-active'));
        }

        document.addEventListener('DOMContentLoaded', function () {
            toggleInputFields();
            const form = document.querySelector('form');
            const loadingIndicator = document.getElementById('loadingIndicator');
            if (form && loadingIndicator) {
                form.addEventListener('submit', function (event) {
                    const textInputVal = document.getElementById('text_input').value.trim();
                    const fileInputFiles = document.getElementById('file').files;
                    const inputType = document.getElementById('input_type').value;
                    let hasInput = false;
                    if (inputType === 'text' && textInputVal) { hasInput = true; }
                    else if ((inputType === 'image' || inputType === 'audio') && fileInputFiles.length > 0) { hasInput = true; }
                    if (hasInput) {
                        loadingIndicator.classList.remove('loading-indicator-hidden');
                    }
                    else {
                        event.preventDefault();
                        alert("Please provide text or upload a file to translate.");
                        loadingIndicator.classList.add('loading-indicator-hidden');
                    }
                });
            }
        });
        // Device ID Management for History Tracking
        function getDeviceId() {
            let deviceId = localStorage.getItem('deviceId');
            if (!deviceId) {
                deviceId = 'device_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9);
                localStorage.setItem('deviceId', deviceId);
            }
            return deviceId;
        }

        // Initialize device on page load
        const DEVICE_ID = getDeviceId();
        console.log('Device ID:', DEVICE_ID);

        // Translated messages for toast notifications
        function getTranslatedMessage(key) {
            const currentLang = localStorage.getItem('uiLanguage') || 'en';
            const messages = {
                'translationSuccess': {
                    'en': 'Translation successful!',
                    'hi': 'अनुवाद सफल!',
                    'bn': 'অনুবাদ সফল!',
                    'ta': 'மொழிபெயர்ப்பு வெற்றிகரமாக!',
                    'te': 'అనువాదం విజయవంతం!',
                    'mr': 'भाषांतर यशस्वी!',
                    'gu': 'અનુવાદ સફળ!',
                    'kn': 'ಅನುವಾದ ಯಶಸ್ವಿ!',
                    'ml': 'വിവർത്തനം വിജയകരം!',
                    'pa': 'ਅਨੁਵਾਦ ਸਫਲ!',
                    'or': 'ଅନୁବାଦ ସଫଳ!'
                },
                'translationFailed': {
                    'en': 'Translation failed',
                    'hi': 'अनुवाद विफल',
                    'bn': 'অনুবাদ ব্যর্থ',
                    'ta': 'மொழிபெயர்ப்பு தோல்வி',
                    'te': 'అనువాదం విఫలమైంది',
                    'mr': 'भाषांतर अयशस्वी',
                    'gu': 'અનુવાદ નિષ્ફળ',
                    'kn': 'ಅನುವಾದ ವಿಫಲವಾಗಿದೆ',
                    'ml': 'വിവർത്തനം പരാജയപ്പെട്ടു',
                    'pa': 'ਅਨੁਵਾਦ ਅਸਫਲ',
                    'or': 'ଅନୁବାଦ ବିଫଳ'
                },
                'playingAudio': {
                    'en': 'Playing audio...',
                    'hi': 'ऑडियो चल रहा है...',
                    'bn': 'অডিও বাজছে...',
                    'ta': 'ஒலி இயங்குகிறது...',
                    'te': 'ఆడియో ప్లే అవుతోంది...',
                    'mr': 'ऑडिओ चालू आहे...',
                    'gu': 'ઓડિયો ચાલી રહ્યો છે...',
                    'kn': 'ಆಡಿಯೊ ಪ್ಲೇ ಆಗುತ್ತಿದೆ...',
                    'ml': 'ഓഡിയോ പ്ലേ ചെയ്യുന്നു...',
                    'pa': 'ਆਡੀਓ ਚੱਲ ਰਿਹਾ ਹੈ...',
                    'or': 'ଅଡିଓ ଚାଲୁଛି...'
                },
                'audioFailed': {
                    'en': 'Audio playback failed',
                    'hi': 'ऑडियो प्लेबैक विफल',
                    'bn': 'অডিও প্লেব্যাক ব্যর্থ',
                    'ta': 'ஒலி இயக்கம் தோல்வி',
                    'te': 'ఆడియో ప్లేబ్యాక్ విఫలమైంది',
                    'mr': 'ऑडिओ प्लेबॅक अयशस्वी',
                    'gu': 'ઓડિયો પ્લેબેક નિષ્ફળ',
                    'kn': 'ಆಡಿಯೊ ಪ್ಲೇಬ್ಯಾಕ್ ವಿಫಲವಾಗಿದೆ',
                    'ml': 'ഓഡിയോ പ്ലേബാക്ക് പരാജയപ്പെട്ടു',
                    'pa': 'ਆਡੀਓ ਪਲੇਬੈਕ ਅਸਫਲ',
                    'or': 'ଅଡିଓ ପ୍ଲେବ୍ୟାକ୍ ବିଫଳ'
                },
                'schemesLoading': {
                    'en': 'Loading schemes...',
                    'hi': 'योजनाएं लोड हो रही हैं...',
                    'bn': 'প্রকল্প লোড হচ্ছে...',
                    'ta': 'திட்டங்கள் ஏற்றப்படுகின்றன...',
                    'te': 'పథకాలు లోడ్ అవుతున్నాయి...',
                    'mr': 'योजना लोड होत आहेत...',
                    'gu': 'યોજનાઓ લોડ થઈ રહી છે...',
                    'kn': 'ಯೋಜನೆಗಳು ಲೋಡ್ ಆಗುತ್ತಿವೆ...',
                    'ml': 'പദ്ധതികൾ ലോഡ് ചെയ്യുന്നു...',
                    'pa': 'ਯੋਜਨਾਵਾਂ ਲੋਡ ਹੋ ਰਹੀਆਂ ਹਨ...',
                    'or': 'ଯୋଜନା ଲୋଡ୍ ହେଉଛି...'
                }
            };

            return messages[key]?.[currentLang] || messages[key]?.['en'] || 'Success';
        }

        // Toast Notification System
        function showToast(message, type = 'success', duration = 3000) {
            const toastContainer = document.getElementById('toastContainer');
            const toast = document.createElement('div');
            toast.className = `toast-notification toast-${type}`;

            const icons = {
                success: '✓',
                error: '✕',
                warning: '⚠',
                info: 'ℹ'
            };

            toast.innerHTML = `
                <span class="toast-icon">${icons[type] || icons.info}</span>
                <span class="toast-message">${message}</span>
            `;

            toastContainer.appendChild(toast);

            // Auto-remove after duration
            setTimeout(() => {
                toast.remove();
            }, duration);
        }

        // Sliding Panel Management
        function openSchemesPanel() {
            console.log('✓ openSchemesPanel() called - V2.0');
            const panel = document.getElementById('schemes-panel');
            const mainContainer = document.getElementById('mainContentContainer');

            console.log('Panel element:', panel);
            console.log('Main container element:', mainContainer);

            panel.classList.add('open');
            if (mainContainer) {
                mainContainer.classList.add('panel-open');
            }

            // Load all schemes
            loadAllSchemes();
        }

        function openSchemesPanelFromCard(schemeId) {
            console.log('✓ openSchemesPanelFromCard() called with scheme:', schemeId, '- V2.0');
            openSchemesPanel();
            // Optionally scroll to that scheme in the panel
            setTimeout(() => {
                const schemeCard = document.querySelector(`[data-scheme-id="${schemeId}"]`);
                if (schemeCard) {
                    schemeCard.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    schemeCard.style.animation = 'highlightScheme 1s ease';
                }
            }, 600);
        }

        function closeSchemesPanel() {
            const panel = document.getElementById('schemes-panel');
            const mainContainer = document.getElementById('mainContentContainer');

            panel.classList.remove('open');
            if (mainContainer) {
                mainContainer.classList.remove('panel-open');
            }
        }

        // Close panel with Escape key
        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape') {
                closeSchemesPanel();
            }
        });

        // Load Daily Schemes (3 rotated daily)
        async function loadDailySchemes() {
            try {
                const response = await fetch('/api/schemes/daily?count=3');
                const data = await response.json();

                if (data.success && data.schemes) {
                    renderDailySchemes(data.schemes);
                }
            } catch (error) {
                console.error('Error loading daily schemes:', error);
            }
        }

        function renderDailySchemes(schemes) {
            const container = document.getElementById('daily-schemes-container');
            if (!container || schemes.length === 0) return;

            // Keep rendering simple, just update if needed
            // For now, keep the existing hardcoded 3 schemes as they match the first 3
        }

        // Load All Schemes (up to 20)
        async function loadAllSchemes() {
            const container = document.getElementById('all-schemes-container');
            const msg = getTranslatedMessage('schemesLoading');
            container.innerHTML = `
                <div class="text-center py-3">
                    <div class="spinner-border spinner-border-sm" style="color: var(--saffron);" role="status">
                        <span class="visually-hidden">Loading...</span>
                    </div>
                    <p class="mt-2 small">${msg}</p>
                </div>
            `;

            try {
                const response = await fetch('/api/schemes/all?limit=20');
                const data = await response.json();

                if (data.success && data.schemes) {
                    await renderAllSchemes(data.schemes);
                } else {
                    container.innerHTML = '<p class="text-center text-danger">Error loading schemes</p>';
                }
            } catch (error) {
                console.error('Error loading all schemes:', error);
                container.innerHTML = '<p class="text-center text-danger">Error loading schemes</p>';
                const msg = getTranslatedMessage('translationFailed');
                showToast(msg, 'error');
            }
        }

        async function renderAllSchemes(schemes) {
            const container = document.getElementById('all-schemes-container');
            const currentLang = localStorage.getItem('uiLanguage') || 'en';

            // Show loading state
            container.innerHTML = `
                <div class="text-center py-3">
                    <div class="spinner-border spinner-border-sm" style="color: var(--saffron);" role="status"></div>
                    <p class="mt-2 small">Loading schemes...</p>
                </div>
            `;

            // Translate schemes if not English
            let translatedSchemes = [];
            if (currentLang !== 'en') {
                translatedSchemes = await translateAllSchemes(schemes, currentLang);
            } else {
                translatedSchemes = schemes;
            }

            const schemesHTML = translatedSchemes.map(scheme => `
                <div class="scheme-card-full" data-scheme-id="${scheme.id}">
                    <div class="d-flex align-items-start">
                        <i class="bi bi-${scheme.icon} scheme-icon"></i>
                        <div class="flex-grow-1">
                            <div class="scheme-title">${scheme.name} - ${scheme.displayFullName || scheme.fullName}</div>
                            <div class="scheme-summary" id="scheme-text-${scheme.id}">${scheme.displaySummary || scheme.summary}</div>
                            <span class="scheme-badge">${scheme.category}</span>
                            
                            <div class="scheme-actions">
                                <button class="btn-audio-scheme-small" onclick="playSchemeAudio('${scheme.id}', event)" title="Listen">
                                    <i class="bi bi-volume-up"></i>
                                </button>
                                <button class="btn-official-link-small" onclick="window.open('${scheme.officialLink}', '_blank')" title="Official Website">
                                    <i class="bi bi-box-arrow-up-right"></i>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            `).join('');

            container.innerHTML = schemesHTML;
        }

        // Instant Scheme Translation
        let translatedSchemes = {}; // Store translated versions
        let allSchemesTranslated = {}; // Cache for all translated schemes

        async function translateAllSchemes(schemes, targetLang) {
            const targetLangMap = {
                'en': 'Hindi',
                'hi': 'Hindi',
                'bn': 'Bengali',
                'ta': 'Tamil',
                'te': 'Telugu',
                'mr': 'Marathi',
                'gu': 'Gujarati',
                'kn': 'Kannada',
                'ml': 'Malayalam',
                'pa': 'Punjabi',
                'or': 'Odia'
            };
            const targetLanguage = targetLangMap[targetLang] || 'Hindi';

            // Check cache
            const cacheKey = `all_${targetLanguage}`;
            if (allSchemesTranslated[cacheKey]) {
                return allSchemesTranslated[cacheKey];
            }

            const translatedResults = [];

            for (const scheme of schemes) {
                try {
                    // Translate full name and summary
                    const fullNameResponse = await fetch('/api/translate/instant', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({
                            text: scheme.fullName,
                            source_lang: 'en',
                            target_lang: targetLanguage
                        })
                    });
                    const fullNameData = await fullNameResponse.json();

                    const summaryResponse = await fetch('/api/translate/instant', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({
                            text: scheme.summary,
                            source_lang: 'en',
                            target_lang: targetLanguage
                        })
                    });
                    const summaryData = await summaryResponse.json();

                    translatedResults.push({
                        ...scheme,
                        displayFullName: fullNameData.success ? fullNameData.translated_text : scheme.fullName,
                        displaySummary: summaryData.success ? summaryData.translated_text : scheme.summary
                    });
                } catch (error) {
                    console.error(`Translation error for ${scheme.id}:`, error);
                    translatedResults.push(scheme);
                }
            }

            // Cache results
            allSchemesTranslated[cacheKey] = translatedResults;
            return translatedResults;
        }

        async function translateSchemeText(schemeId, event) {
            event.stopPropagation();

            const button = event.target.closest('button');
            const originalText = button.innerHTML;
            button.disabled = true;
            button.innerHTML = '<span class="spinner-border spinner-border-sm"></span> Translating...';

            try {
                // Get current UI language or use Hindi as default target
                const currentLang = localStorage.getItem('uiLanguage') || 'en';
                const targetLangMap = {
                    'en': 'Hindi',
                    'hi': 'Hindi',
                    'bn': 'Bengali',
                    'ta': 'Tamil',
                    'te': 'Telugu',
                    'mr': 'Marathi',
                    'gu': 'Gujarati',
                    'kn': 'Kannada',
                    'ml': 'Malayalam',
                    'pa': 'Punjabi',
                    'or': 'Odia'
                };
                const targetLang = targetLangMap[currentLang] || 'Hindi';

                // Fetch scheme details
                const schemeResponse = await fetch(`/api/schemes/${schemeId}`);
                const schemeData = await schemeResponse.json();

                if (!schemeData.success) {
                    throw new Error('Scheme not found');
                }

                const scheme = schemeData.scheme;
                const textToTranslate = `${scheme.fullName}. ${scheme.summary}`;

                // Check if already translated
                const cacheKey = `${schemeId}_${targetLang}`;
                if (translatedSchemes[cacheKey]) {
                    updateSchemeCardText(schemeId, translatedSchemes[cacheKey]);
                    showToast(`Translated to ${targetLang}`, 'success');
                    button.disabled = false;
                    button.innerHTML = originalText;
                    return;
                }

                // Call instant translation API
                const response = await fetch('/api/translate/instant', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        text: textToTranslate,
                        source_lang: 'en',
                        target_lang: targetLang
                    })
                });

                const data = await response.json();

                if (data.success) {
                    translatedSchemes[cacheKey] = data.translated_text;
                    updateSchemeCardText(schemeId, data.translated_text);
                    showToast(`Translated to ${targetLang}`, 'success');
                } else {
                    throw new Error(data.error || 'Translation failed');
                }
            } catch (error) {
                console.error('Translation error:', error);
                showToast('Translation failed: ' + error.message, 'error');
            } finally {
                button.disabled = false;
                button.innerHTML = originalText;
            }
        }

        function updateSchemeCardText(schemeId, translatedText) {
            const card = document.querySelector(`[data-scheme-id="${schemeId}"]`);
            if (card) {
                const summaryDiv = card.querySelector('.scheme-summary');
                if (summaryDiv) {
                    summaryDiv.textContent = translatedText;
                    summaryDiv.style.fontStyle = 'italic';
                }
            }
        }

        // Play Scheme Audio with text highlighting
        async function playSchemeAudio(schemeId, event) {
            event.stopPropagation();

            const button = event.target.closest('button');
            const originalText = button.innerHTML;
            button.disabled = true;
            button.innerHTML = '<span class="spinner-border spinner-border-sm"></span>';

            try {
                // Get current UI language
                const currentLang = localStorage.getItem('uiLanguage') || 'en';
                const ttsLangMap = {
                    'en': 'en',
                    'hi': 'hi',
                    'bn': 'bn',
                    'ta': 'ta',
                    'te': 'te',
                    'mr': 'mr',
                    'gu': 'gu',
                    'kn': 'kn',
                    'ml': 'ml',
                    'pa': 'pa',
                    'or': 'en' // Odia not supported, fallback to English
                };
                const ttsLang = ttsLangMap[currentLang] || 'en';

                // Get scheme text (translated if available, otherwise original)
                const textContainerId = `scheme-text-${schemeId}`;
                const summaryDiv = document.getElementById(textContainerId);
                const text = summaryDiv.textContent;

                // Create form data for TTS request
                const formData = new URLSearchParams();
                formData.append('text', text);
                formData.append('lang', ttsLang);

                const response = await fetch('/tts', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded'
                    },
                    body: formData
                });

                if (!response.ok) {
                    throw new Error('Audio generation failed');
                }

                const blob = await response.blob();
                const audioUrl = URL.createObjectURL(blob);
                const audio = new Audio(audioUrl);

                // Setup word highlighting
                setupWordHighlightingForScheme(audio, textContainerId, text);

                audio.play();
                const msg = getTranslatedMessage('playingAudio');
                showToast(msg, 'info', 2000);

                audio.onended = () => {
                    URL.revokeObjectURL(audioUrl);
                    clearWordHighlighting(textContainerId);
                    button.disabled = false;
                    button.innerHTML = originalText;
                };

                audio.onerror = () => {
                    URL.revokeObjectURL(audioUrl);
                    clearWordHighlighting(textContainerId);
                    button.disabled = false;
                    button.innerHTML = originalText;
                    const msg = getTranslatedMessage('audioFailed');
                    showToast(msg, 'error');
                };

            } catch (error) {
                console.error('Audio error:', error);
                const msg = getTranslatedMessage('audioFailed');
                showToast(msg, 'error');
                button.disabled = false;
                button.innerHTML = originalText;
            }
        }

        function setupWordHighlightingForScheme(audioPlayer, textContainerId, text) {
            const textContainer = document.getElementById(textContainerId);
            if (!textContainer) return;

            const originalText = text;
            const words = text.split(/\s+/).filter(w => w.length > 0);

            const baseCharsPerSecond = 12;
            let cumulativeTime = 0;
            const wordTimings = words.map(word => {
                const hasPunctuation = /[.!?,;:]$/.test(word);
                const wordDuration = (word.length / baseCharsPerSecond) + (hasPunctuation ? 0.3 : 0);
                const startTime = cumulativeTime;
                cumulativeTime += wordDuration;
                return { word, startTime, endTime: cumulativeTime };
            });

            textContainer.innerHTML = words.map((word, index) =>
                `<span class="tts-word" data-word-index="${index}">${word}</span>`
            ).join(' ');

            const wordSpans = textContainer.querySelectorAll('.tts-word');
            let animationFrameId = null;

            const updateHighlight = () => {
                if (audioPlayer.paused || audioPlayer.ended) return;

                const currentTime = audioPlayer.currentTime;
                const totalDuration = audioPlayer.duration;
                const timeScale = totalDuration / cumulativeTime;

                wordSpans.forEach(span => span.classList.remove('tts-word-active'));

                for (let i = 0; i < wordTimings.length; i++) {
                    const scaledStart = wordTimings[i].startTime * timeScale;
                    const scaledEnd = wordTimings[i].endTime * timeScale;

                    if (currentTime >= scaledStart && currentTime < scaledEnd) {
                        wordSpans[i].classList.add('tts-word-active');
                        break;
                    }
                }

                animationFrameId = requestAnimationFrame(updateHighlight);
            };

            audioPlayer.addEventListener('play', () => {
                if (animationFrameId) cancelAnimationFrame(animationFrameId);
                updateHighlight();
            });

            audioPlayer.addEventListener('pause', () => {
                if (animationFrameId) {
                    cancelAnimationFrame(animationFrameId);
                    animationFrameId = null;
                }
            });

            audioPlayer.addEventListener('ended', () => {
                if (animationFrameId) cancelAnimationFrame(animationFrameId);
                textContainer.innerHTML = originalText;
            });
        }

        // Instant File Translation (Non-blocking)
        async function instantFileTranslation(file, inputType, targetLanguage) {
            const loadingOverlay = document.getElementById('loadingOverlay');
            loadingOverlay.classList.add('active');

            try {
                const formData = new FormData();
                formData.append('file', file);
                formData.append('input_type', inputType);
                formData.append('target_language', targetLanguage);
                formData.append('device_id', DEVICE_ID);

                const response = await fetch('/api/translate/file', {
                    method: 'POST',
                    body: formData
                });

                const data = await response.json();

                if (data.success) {
                    showToast('File translated successfully!', 'success');

                    // Display results dynamically (you can enhance this)
                    displayTranslationResult(data);
                } else {
                    throw new Error(data.error || 'Translation failed');
                }
            } catch (error) {
                console.error('File translation error:', error);
                showToast('File translation failed: ' + error.message, 'error');
            } finally {
                loadingOverlay.classList.remove('active');
            }
        }

        function displayTranslationResult(data) {
            // This would dynamically update the page with results
            // For simplicity, showing a toast - you can enhance this
            console.log('Translation result:', data);
        }

        // Initialize on page load
        document.addEventListener('DOMContentLoaded', function () {
            console.log('✅ DOM fully loaded - V2.0');
            console.log('✅ onclick handlers should be active now');
            console.log('Test: Click PM-KISAN, PMFBY, or KCC cards, or the View All button');

            // Load daily schemes
            loadDailySchemes();

            // Restore UI language
            const savedLang = localStorage.getItem('uiLanguage');
            if (savedLang) {
                changeUILanguage(savedLang);
            }

            // Translate history section labels
            translateHistoryLabels();
        });

        // Translate history section labels based on UI language
        function translateHistoryLabels() {
            const currentLang = localStorage.getItem('uiLanguage') || 'en';
            const historyTranslations = {
                'activityHeader': {
                    'en': '🕐 Activity Log',
                    'hi': '🕐 गतिविधि लॉग | Activity Log',
                    'bn': '🕐 কার্যকলাপ লগ',
                    'ta': '🕐 செயல்பாடு பதிவு',
                    'te': '🕐 కార్యాచరణ లాగ్',
                    'mr': '🕐 क्रियाकलाप लॉग',
                    'gu': '🕐 પ્રવૃત્તિ લોગ',
                    'kn': '🕐 ಚಟುವಟಿಕೆ ದಾಖಲೆ',
                    'ml': '🕐 പ്രവർത്തന രേഖ',
                    'pa': '🕐 ਗਤੀਵਿਧੀ ਲਾੱਗ',
                    'or': '🕐 କାର୍ଯ୍ୟକଳାପ ଲଗ୍'
                },
                'success': {
                    'en': 'Success',
                    'hi': 'सफल',
                    'bn': 'সফল',
                    'ta': 'வெற்றி',
                    'te': 'విజయం',
                    'mr': 'यशस्वी',
                    'gu': 'સફળ',
                    'kn': 'ಯಶಸ್ಸು',
                    'ml': 'വിജയം',
                    'pa': 'ਸਫਲ',
                    'or': 'ସଫଳ'
                },
                'failed': {
                    'en': 'Failed',
                    'hi': 'विफल',
                    'bn': 'ব্যর্থ',
                    'ta': 'தோல்வி',
                    'te': 'విఫలమైంది',
                    'mr': 'अयशस्वी',
                    'gu': 'નિષ્ફળ',
                    'kn': 'ವಿಫಲವಾಗಿದೆ',
                    'ml': 'പരാജയം',
                    'pa': 'ਅਸਫਲ',
                    'or': 'ବିଫଳ'
                },
                'timestamp': {
                    'en': 'Timestamp',
                    'hi': 'समय',
                    'bn': 'সময়',
                    'ta': 'நேரம்',
                    'te': 'సమయం',
                    'mr': 'वेळ',
                    'gu': 'સમય',
                    'kn': 'ಸಮಯ',
                    'ml': 'സമയം',
                    'pa': 'ਸਮਾਂ',
                    'or': 'ସମୟ'
                },
                'originalText': {
                    'en': 'Original Text',
                    'hi': 'मूल पाठ',
                    'bn': 'মূল পাঠ',
                    'ta': 'அசல் உரை',
                    'te': 'అసలు వచనం',
                    'mr': 'मूळ मजकूर',
                    'gu': 'મૂળ લખાણ',
                    'kn': 'ಮೂಲ ಪಠ್ಯ',
                    'ml': 'യഥാർത്ഥ വാചകം',
                    'pa': 'ਅਸਲ ਪਾਠ',
                    'or': 'ମୂଳ ପାଠ'
                },
                'translatedText': {
                    'en': 'Translated Text',
                    'hi': 'अनुवादित पाठ',
                    'bn': 'অনূদিত পাঠ',
                    'ta': 'மொழிபெயர்க்கப்பட்ட உரை',
                    'te': 'అనువదించిన వచనం',
                    'mr': 'भाषांतरित मजकूर',
                    'gu': 'અનુવાદિત લખાણ',
                    'kn': 'ಅನುವಾದಿತ ಪಠ್ಯ',
                    'ml': 'വിവർത്തനം ചെയ്ത വാചകം',
                    'pa': 'ਅਨੁਵਾਦ ਕੀਤਾ ਪਾਠ',
                    'or': 'ଅନୁବାଦିତ ପାଠ'
                },
                'listen': {
                    'en': 'Listen',
                    'hi': 'सुनें',
                    'bn': 'শুনুন',
                    'ta': 'கேள்',
                    'te': 'వినండి',
                    'mr': 'ऐका',
                    'gu': 'સાંભળો',
                    'kn': 'ಕೇಳಿ',
                    'ml': 'കേൾക്കുക',
                    'pa': 'ਸੁਣੋ',
                    'or': 'ଶୁଣନ୍ତୁ'
                },
                'error': {
                    'en': 'Error',
                    'hi': 'त्रुटि',
                    'bn': 'ত্রুটি',
                    'ta': 'பிழை',
                    'te': 'లోపం',
                    'mr': 'त्रुटी',
                    'gu': 'ભૂલ',
                    'kn': 'ದೋಷ',
                    'ml': 'പിശക്',
                    'pa': 'ਗਲਤੀ',
                    'or': 'ତ୍ରୁଟି'
                }
            };

            // Update activity header if exists
            const activityHeaders = document.querySelectorAll('[data-i18n="activity.header"]');
            activityHeaders.forEach(header => {
                if (historyTranslations.activityHeader[currentLang]) {
                    header.textContent = historyTranslations.activityHeader[currentLang];
                }
            });

            // Update badge texts in history
            document.querySelectorAll('.accordion-button .badge').forEach(badge => {
                const text = badge.textContent.trim();
                if (text.includes('Success') || text.includes('सफल')) {
                    badge.textContent = historyTranslations.success[currentLang] || 'Success';
                } else if (text.includes('Failed') || text.includes('विफल')) {
                    badge.textContent = historyTranslations.failed[currentLang] || 'Failed';
                }
            });
        }
