import re

def validate_abstract(abstract: str) -> dict:
   
    response = {
        "valid": True,
        "errors": []
    }
    
    # 1. التحقق من نوع البيانات المدخلة
    if not isinstance(abstract, str):
        return {"valid": False, "errors": ["Input must be a valid text string."]}
    
    # 2. تنظيف النص من الفراغات الزائدة في الأول والآخر
    abstract = abstract.strip()
    
    # 3. التحقق من النص الفارغ
    if not abstract:
        return {"valid": False, "errors": ["Abstract cannot be empty."]}
    
    # 4. حساب عدد الكلمات بدقة باستخدام Regex عشان نتفادى المسافات الزائدة والسطور الجديدة
    words = re.findall(r"\b\w+\b", abstract)
    word_count = len(words)
    
    # 5. تطبيق شروط المجلة (بين 200 و 300 كلمة)
    if word_count < 200:
        response["valid"] = False
        response["errors"].append(f"Abstract is too short ({word_count} words). Minimum required is 200 words.")
    elif word_count > 300:
        response["valid"] = False
        response["errors"].append(f"Abstract is too long ({word_count} words). Maximum allowed is 300 words.")
        
    return response


# --- تجربة الكود واختباره (Main) ---
def main_task3():
    print("=" * 20 + " Task 3: Abstract Validator " + "=" * 20)
    
    # مثال لنص قصير جداً
    short_abstract = "This is a very short abstract animation snippet."
    
    # مثال لنص مثالي (هنكرر جملة عشان نوصل لـ 210 كلمة)
    good_abstract = " ".join(["The study of sustainable development in digital platforms is crucial for future eco-smart innovations."] * 15)
    
    test_cases = [short_abstract, good_abstract, "", None]
    
    for idx, case in enumerate(test_cases, 1):
        print(f"\nTest Case {idx}:")
        result = validate_abstract(case)
        print(f"Result: {result}")

if __name__ == "__main__":
    main_task3()