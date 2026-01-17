import os
import shutil

def sovereign_cleanup():
    # القائمة البيضاء: الملفات والمجلدات المحرم لمسها
    sacred_list = [
        "main.py", 
        "buildozer.spec", 
        ".sovereign_logic.bin",  # نظام الخبرة
        "experience.json",
        "bin",                   # مجلد الألعاب الجاهزة (APK/OBB)
        "clean.py"
    ]

    print("--- [ بداية عملية التطهير السيادي ] ---")
    
    # المسارات التي سيتم فحصها وتنظيفها
    current_dir = os.getcwd()
    
    files_deleted = 0
    folders_deleted = 0

    for item in os.listdir(current_dir):
        # تخطي الملفات الموجودة في القائمة البيضاء
        if item in sacred_list:
            continue
            
        item_path = os.path.join(current_dir, item)
        
        try:
            if os.path.isfile(item_path):
                os.remove(item_path)
                print(f"[حذف ملف]: {item}")
                files_deleted += 1
            elif os.path.isdir(item_path):
                # استثناء مجلد bin لأنه يحتوي على نتاج العمل
                if item == "bin": continue
                
                shutil.rmtree(item_path)
                print(f"[حذف مجلد مؤقت]: {item}")
                folders_deleted += 1
        except Exception as e:
            print(f"[خطأ]: لم يتمكن المهندس من حذف {item} - {e}")

    print("---------------------------------------")
    print(f"تم التطهير بنجاح!")
    print(f"الملفات المحذوفة: {files_deleted} | المجلدات المحذوفة: {folders_deleted}")
    print("الخبرات والأكواد والحزم (APK+OBB) في أمان مطلق.")
    print("---------------------------------------")

if __name__ == "__main__":
    sovereign_cleanup()

