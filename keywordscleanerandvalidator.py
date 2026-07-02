import re

def clean_and_validate_keywords(keywords_raw: str, min_count: int = 3, max_count: int = 6) -> dict:
 
    response = {
        "valid": True,
        "cleaned_keywords": [],
        "errors": []
    }
    
    # 1. التحقق من نوع البيانات المدخلة
    if not isinstance(keywords_raw, str):
        return {"valid": False, "cleaned_keywords": [], "errors": ["Keywords must be a valid text string."]}
        
    # 2. فصل الكلمات بناءً على الفواصل سواء كانت عادية , أو منقوطة ; لتسهيل تجربة المستخدم
    # واستخدام الـ Regex لتنظيف المسافات المحيطة بالكلمة فوراً
    raw_list = re.split(r'[;,]', keywords_raw)
    
    cleaned_list = []
    for kw in raw_list:
        cleaned_kw = kw.strip().lower() # تنظيف الفراغات وتحويل الحروف لـ lowercase لتوحيد الفهرسة
        if cleaned_kw: # نتأكد إن الكلمة مش فاضية (عشان لو فيه فاصلة زيادة ورا بعض)
            cleaned_list.append(cleaned_kw)
            
    response["cleaned_keywords"] = cleaned_list
    
    # 3. التحقق من عدد الكلمات المفتاحية حسب معايير المجلة
    total_keywords = len(cleaned_list)
    
    if total_keywords < min_count:
        response["valid"] = False
        response["errors"].append(f"Too few keywords ({total_keywords}). System requires between {min_count} and {max_count} keywords.")
    elif total_keywords > max_count:
        response["valid"] = False
        response["errors"].append(f"Too many keywords ({total_keywords}). System requires between {min_count} and {max_count} keywords.")
        
    return response


# --- تجربة الكود واختباره (Main) ---
def main_task4():
    print("\n" + "=" * 20 + " Task 4: Keywords Cleaner " + "=" * 20)
    
    # مدخلات عشوائية من مستخدم (مسافات وحروف كابيتال وفواصل زيادة)
    dirty_input = "  FastAPI ,  bCrypt ; machine Learning, Data Science, AI  "
    too_short_input = "Chemistry, Science"
    
    test_cases = [dirty_input, too_short_input, None]
    
    for idx, case in enumerate(test_cases, 1):
        print(f"\nTest Case {idx}:")
        result = clean_and_validate_keywords(case)
        print(f"Result: {result}")

if __name__ == "__main__":
    main_task4()