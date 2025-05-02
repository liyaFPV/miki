import os
import json

def get_config():
    file_path='config.json'
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            config = json.load(file)
        return config
    except FileNotFoundError:
        print(f"Ошибка: Файл {file_path} не найден.")
        return {}
    except json.JSONDecodeError:
        print(f"Ошибка: Файл {file_path} содержит некорректный JSON.")
        return {}
    



def load_commands():
    config = get_config()
    root_dir=config.get('command_dir')
    commands_expanded = []
    
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        data = json.load(f)
                        if not all(key in data for key in ["text", "type", "run"]):
                            print(f"Ошибка: В файле {file_path} нет нужных полей!")
                            continue

                        # Берём первый элемент run, если это массив, иначе сам run (как строку)
                        run_command = data["run"][0] if isinstance(data["run"], list) else data["run"]
                        saynem = data.get("saynem")  # Опциональный параметр

                        for phrase in data["text"]:
                            command = {
                                "text": phrase,
                                "type": data["type"],
                                "run": run_command  # Теперь всегда строка
                            }
                            if saynem is not None:
                                command["saynem"] = saynem
                            commands_expanded.append(command)
                except Exception as e:
                    print(f"Ошибка при чтении {file_path}: {e}")
    
    return commands_expanded

