# schemes_data.py - Government Farming Schemes Database
from datetime import datetime

# Government Schemes with details
GOVERNMENT_SCHEMES = [
    {
        "id": "pm-kisan",
        "name": "PM-KISAN",
        "fullName": "Pradhan Mantri Kisan Samman Nidhi",
        "icon": "cash-coin",
        "summary": "Direct income support of ₹6000/year to all farmers with cultivable land. Payment in 3 installments of ₹2000 each.",
        "description": "The PM-KISAN scheme provides income support to all landholding farmers' families across the country to supplement their financial needs for procuring various inputs related to agriculture and allied activities as well as domestic needs.",
        "benefits": "₹6000 per year in 3 equal installments",
        "eligibility": "All landholding farmers' families",
        "officialLink": "https://pmkisan.gov.in/",
        "regions": ["All India"],
        "category": "Direct Benefit Transfer",
        "lastUpdated": "2024-01-15"
    },
    {
        "id": "pmfby",
        "name": "PMFBY",
        "fullName": "Pradhan Mantri Fasal Bima Yojana",
        "icon": "shield-check",
        "summary": "Comprehensive crop insurance scheme covering pre-sowing to post-harvest losses. Low premium rates with high coverage.",
        "description": "PMFBY provides insurance coverage and financial support to farmers in case of crop failure. It aims to stabilize farmers' income and encourage adoption of innovative farming practices.",
        "benefits": "Up to 200% of sum insured for crop loss",
        "eligibility": "All farmers including sharecroppers and tenant farmers",
        "officialLink": "https://pmfby.gov.in/",
        "regions": ["All India"],
        "category": "Insurance",
        "lastUpdated": "2024-01-20"
    },
    {
        "id": "kcc",
        "name": "KCC",
        "fullName": "Kisan Credit Card",
        "icon": "credit-card-2-front",
        "summary": "Easy credit facility for agriculture needs. Low interest rates, flexible repayment, and insurance coverage included.",
        "description": "KCC provides farmers with timely and adequate credit for their farming operations and consumption needs. The card offers a flexible and hassle-free credit facility.",
        "benefits": "Up to ₹3 lakh credit at 4% interest",
        "eligibility": "All farmers with land ownership or cultivation rights",
        "officialLink": "https://www.india.gov.in/spotlight/kisan-credit-card-kcc",
        "regions": ["All India"],
        "category": "Credit Facility",
        "lastUpdated": "2024-01-18"
    },
    {
        "id": "pm-kusum",
        "name": "PM-KUSUM",
        "fullName": "Pradhan Mantri Kisan Urja Suraksha evam Utthaan Mahabhiyan",
        "icon": "sun",
        "summary": "Solar energy for farmers - install solar pumps and generate additional income by selling surplus power.",
        "description": "PM-KUSUM aims to add solar capacity of 25,750 MW by 2022 with total central financial support of ₹34,422 Crore. Farmers can install solar pumps and grid-connected solar power plants.",
        "benefits": "90% subsidy on solar pump installation",
        "eligibility": "Individual farmers and farmer groups",
        "officialLink": "https://mnre.gov.in/solar/schemes/",
        "regions": ["All India"],
        "category": "Solar Energy",
        "lastUpdated": "2024-01-12"
    },
    {
        "id": "soil-health-card",
        "name": "Soil Health Card",
        "fullName": "Soil Health Card Scheme",
        "icon": "flower1",
        "summary": "Get detailed soil analysis and customized fertilizer recommendations for better crop yield.",
        "description": "Soil Health Cards provide information to farmers on nutrient status of their soil along with recommendations on appropriate dosage of nutrients for improving soil health and fertility.",
        "benefits": "Free soil testing every 2 years",
        "eligibility": "All farmers",
        "officialLink": "https://soilhealth.dac.gov.in/",
        "regions": ["All India"],
        "category": "Soil Management",
        "lastUpdated": "2024-01-10"
    },
    {
        "id": "paramparagat-krishi",
        "name": "PKVY",
        "fullName": "Paramparagat Krishi Vikas Yojana",
        "icon": "egg",
        "summary": "Financial assistance for organic farming. Promotes traditional farming practices with modern techniques.",
        "description": "PKVY promotes organic farming through cluster approach and Participatory Guarantee System (PGS) certification. It aims to increase domestic production and certification of organic produce.",
        "benefits": "₹50,000 per hectare for 3 years",
        "eligibility": "Farmers willing to adopt organic farming",
        "officialLink": "https://pgsindia-ncof.gov.in/",
        "regions": ["All India"],
        "category": "Organic Farming",
        "lastUpdated": "2024-01-08"
    },
    {
        "id": "mgnrega",
        "name": "MGNREGA",
        "fullName": "Mahatma Gandhi National Rural Employment Guarantee Act",
        "icon": "people",
        "summary": "Guaranteed 100 days of wage employment for rural households. Enhances livelihood security in rural areas.",
        "description": "MGNREGA guarantees 100 days of employment in a financial year to adult members of rural households willing to do unskilled manual work at statutory minimum wage.",
        "benefits": "100 days guaranteed wage employment per year",
        "eligibility": "Rural households",
        "officialLink": "https://nrega.nic.in/",
        "regions": ["All India - Rural"],
        "category": "Employment",
        "lastUpdated": "2024-01-25"
    },
    {
        "id": "pm-aasha",
        "name": "PM-AASHA",
        "fullName": "Pradhan Mantri Annadata Aay Sanrakshan Abhiyan",
        "icon": "basket",
        "summary": "Ensures Minimum Support Price (MSP) to farmers for their produce. Protects farmers from price fluctuations.",
        "description": "PM-AASHA is an umbrella scheme with three components: Price Support Scheme (PSS), Price Deficiency Payment Scheme (PDPS), and Pilot of Private Procurement & Stockist Scheme (PPPS).",
        "benefits": "MSP guarantee for 23 crops",
        "eligibility": "All farmers growing notified crops",
        "officialLink": "https://agricoop.gov.in/",
        "regions": ["All India"],
        "category": "Price Support",
        "lastUpdated": "2024-01-22"
    },
    {
        "id": "pmkvy",
        "name": "PMKVY",
        "fullName": "Pradhan Mantri Kaushal Vikas Yojana",
        "icon": "award",
        "summary": "Skill development training for rural youth. Focus on agriculture and allied sectors.",
        "description": "PMKVY provides industry-relevant skill training to youth. Special focus on agriculture sector skills including modern farming techniques, dairy farming, horticulture, and more.",
        "benefits": "Free skill training with certification",
        "eligibility": "Rural youth aged 18-35 years",
        "officialLink": "https://www.pmkvyofficial.org/",
        "regions": ["All India"],
        "category": "Skill Development",
        "lastUpdated": "2024-01-14"
    },
    {
        "id": "pmfme",
        "name": "PMFME",
        "fullName": "Pradhan Mantri Formalisation of Micro Food Processing Enterprises",
        "icon": "shop",
        "summary": "Support for micro food processing enterprises. Credit subsidy and technical assistance included.",
        "description": "PMFME aims to enhance competitiveness of existing micro food processing enterprises and support formalization of the sector. It provides financial, technical, and business support.",
        "benefits": "35% credit-linked subsidy up to ₹10 lakh",
        "eligibility": "Individual entrepreneurs, SHGs, FPOs, cooperatives",
        "officialLink": "https://pmfme.mofpi.gov.in/",
        "regions": ["All India"],
        "category": "Food Processing",
        "lastUpdated": "2024-01-16"
    },
    {
        "id": "nmmi",
        "name": "NMMI",
        "fullName": "National Mission on Edible Oils - Oil Palm",
        "icon": "droplet",
        "summary": "Promote oil palm cultivation to reduce import dependency. Financial assistance for plantation.",
        "description": "The mission aims to increase palm oil production and reduce India's dependence on imports. It provides financial assistance for area expansion and productivity improvement.",
        "benefits": "₹29,000 per hectare for cultivation",
        "eligibility": "Farmers in suitable agro-climatic zones",
        "officialLink": "https://nmoop.gov.in/",
        "regions": ["Andhra Pradesh, Telangana, Karnataka, Tamil Nadu, Gujarat, Mizoram, Assam"],
        "category": "Oilseeds",
        "lastUpdated": "2024-01-11"
    },
    {
        "id": "pmay-g",
        "name": "PMAY-G",
        "fullName": "Pradhan Mantri Awaas Yojana - Gramin",
        "icon": "house",
        "summary": "Housing for all in rural areas. Financial assistance for building pucca houses.",
        "description": "PMAY-G aims to provide pucca houses with basic amenities to all houseless and households living in kutcha/dilapidated houses in rural areas by 2024.",
        "benefits": "₹1.20-1.30 lakh assistance for house construction",
        "eligibility": "Rural families without pucca house",
        "officialLink": "https://pmayg.nic.in/",
        "regions": ["All India - Rural"],
        "category": "Housing",
        "lastUpdated": "2024-01-19"
    },
    {
        "id": "kalia",
        "name": "KALIA",
        "fullName": "Krushak Assistance for Livelihood and Income Augmentation",
        "icon": "cash-stack",
        "summary": "Odisha state scheme for comprehensive support to farmers. Includes financial assistance and insurance.",
        "description": "KALIA provides comprehensive support to farmers and landless agricultural households. It includes cultivation support, livelihood support, life insurance, and interest-free crop loans.",
        "benefits": "₹25,000 per family over 5 seasons",
        "eligibility": "Small and marginal farmers in Odisha",
        "officialLink": "https://kalia.odisha.gov.in/",
        "regions": ["Odisha"],
        "category": "State Scheme",
        "lastUpdated": "2024-01-13"
    },
    {
        "id": "rythu-bandhu",
        "name": "Rythu Bandhu",
        "fullName": "Rythu Bandhu Scheme",
        "icon": "currency-rupee",
        "summary": "Telangana state investment support scheme. Direct financial assistance for crop cultivation.",
        "description": "Rythu Bandhu provides investment support to farmers for purchase of inputs like seeds, fertilizers, pesticides, labor, and other investments for agriculture and horticulture crops.",
        "benefits": "₹10,000 per acre per year",
        "eligibility": "All landholding farmers in Telangana",
        "officialLink": "https://rythubandhu.telangana.gov.in/",
        "regions": ["Telangana"],
        "category": "State Scheme",
        "lastUpdated": "2024-01-17"
    },
    {
        "id": "pm-smy",
        "name": "PM-SMY",
        "fullName": "Pradhan Mantri Sampada Yojana",
        "icon": "truck",
        "summary": "Support for food processing industries. Creates modern infrastructure with efficient supply chain.",
        "description": "PM Sampada Yojana is a comprehensive package for creating modern infrastructure with efficient supply chain management from farm gate to retail outlet for food processing.",
        "benefits": "Grant-in-aid for infrastructure development",
        "eligibility": "Food processing enterprises and farmer groups",
        "officialLink": "https://www.mofpi.gov.in/Schemes/pradhan-mantri-kisan-sampada-yojana",
        "regions": ["All India"],
        "category": "Infrastructure",
        "lastUpdated": "2024-01-09"
    },
    {
        "id": "nmsa",
        "name": "NMSA",
        "fullName": "National Mission for Sustainable Agriculture",
        "icon": "tree",
        "summary": "Promotes sustainable agriculture practices. Focus on soil health, water efficiency, and climate resilience.",
        "description": "NMSA aims to make agriculture more productive, sustainable, remunerative and climate resilient by promoting location specific integrated farming systems and adopting sustainable farming practices.",
        "benefits": "Subsidy for water conservation and soil health management",
        "eligibility": "All farmers",
        "officialLink": "https://nmsa.dac.gov.in/",
        "regions": ["All India"],
        "category": "Sustainable Agriculture",
        "lastUpdated": "2024-01-21"
    },
    {
        "id": "smam",
        "name": "SMAM",
        "fullName": "Sub-Mission on Agricultural Mechanization",
        "icon": "gear",
        "summary": "Financial assistance for purchasing agricultural machinery and equipment. Promotes farm mechanization.",
        "description": "SMAM aims to increase the reach of farm mechanization to small and marginal farmers and to regions where farm power availability is low. Provides subsidy for purchasing equipment.",
        "benefits": "40-50% subsidy on agricultural machinery",
        "eligibility": "Individual farmers, FPOs, and CHCs",
        "officialLink": "https://agrimachinery.nic.in/",
        "regions": ["All India"],
        "category": "Farm Mechanization",
        "lastUpdated": "2024-01-23"
    },
    {
        "id": "nfsm",
        "name": "NFSM",
        "fullName": "National Food Security Mission",
        "icon": "bag",
        "summary": "Increase production of rice, wheat, pulses, and coarse cereals. Provides technical support and inputs.",
        "description": "NFSM aims to increase production and productivity of selected crops through area expansion and productivity enhancement in a sustainable manner.",
        "benefits": "Free seeds, technical support, and input subsidies",
        "eligibility": "All farmers",
        "officialLink": "https://nfsm.gov.in/",
        "regions": ["All India"],
        "category": "Food Security",
        "lastUpdated": "2024-01-24"
    },
    {
        "id": "nhdp",
        "name": "NHDP",
        "fullName": "National Horticulture Development Program",
        "icon": "flower2",
        "summary": "Develop horticulture sector with focus on fruits, vegetables, spices, and flowers. Market linkages provided.",
        "description": "NHDP provides holistic growth of horticulture sector covering fruits, vegetables, root and tuber crops, mushrooms, spices, flowers, aromatic plants, cashew and cocoa.",
        "benefits": "Subsidy for planting material, protected cultivation, and post-harvest infrastructure",
        "eligibility": "All horticulture farmers and entrepreneurs",
        "officialLink": "https://midh.gov.in/",
        "regions": ["All India"],
        "category": "Horticulture",
        "lastUpdated": "2024-01-26"
    },
    {
        "id": "rashtriya-gokul",
        "name": "Rashtriya Gokul Mission",
        "fullName": "Rashtriya Gokul Mission",
        "icon": "heart-pulse",
        "summary": "Conservation and development of indigenous bovine breeds. Genetic improvement and breed multiplication.",
        "description": "The mission aims at conservation and development of indigenous breeds through selective breeding and genetic up-gradation of cattle and buffaloes.",
        "benefits": "Financial assistance for breed conservation centers",
        "eligibility": "Dairy farmers and indigenous breed owners",
        "officialLink": "https://dahd.nic.in/schemes/programmes/rashtriya-gokul-mission",
        "regions": ["All India"],
        "category": "Animal Husbandry",
        "lastUpdated": "2024-01-27"
    }
]

def get_schemes(limit=None):
    """Get government schemes, optionally limited to a specific count"""
    schemes = GOVERNMENT_SCHEMES.copy()
    if limit:
        return schemes[:limit]
    return schemes

def get_scheme_by_id(scheme_id):
    """Get a specific scheme by its ID"""
    for scheme in GOVERNMENT_SCHEMES:
        if scheme['id'] == scheme_id:
            return scheme
    return None

def get_daily_schemes(count=3):
    """Get schemes for daily display (rotates based on date)"""
    from datetime import date
    day_of_year = date.today().timetuple().tm_yday
    start_index = day_of_year % len(GOVERNMENT_SCHEMES)
    
    schemes = []
    for i in range(count):
        index = (start_index + i) % len(GOVERNMENT_SCHEMES)
        schemes.append(GOVERNMENT_SCHEMES[index])
    
    return schemes
