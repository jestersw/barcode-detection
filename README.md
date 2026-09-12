# Считывание штрихкодов на конвейере: демонстрационный прототип

Демо реализует ядро алгоритма: распознавание штрихкодов на
изображении и сборку всех кодов одной коробки в единый результат с
дедупликацией. 


Декодирование выполняет ZBar (`pyzbar`). Детектор подключаемый: при передаче
обученных весов YOLO активируется локализация, иначе используется фолбэк на
полный кадр.

## Требования

- Python 3.10+
- Homebrew

## Установка (macOS)

Установить библиотеку zbar:
```sh
brew install zbar
```

Создать виртуальное окружение и поставить зависимости:
```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Указать путь к библиотеке zbar (иначе pyzbar не найдет ее при декодировании):
```sh
export DYLD_LIBRARY_PATH=$(brew --prefix zbar)/lib:$DYLD_LIBRARY_PATH
```

## Запуск

Для генерации тестовых изображений понадобятся два пакета:
```sh
pip install python-barcode pillow
```

Сгенерировать тестовый штрихкод EAN-13:
```sh
python -c "import barcode; from barcode.writer import ImageWriter; barcode.get('ean13', '246528561310', writer=ImageWriter()).save('sample')"
```

Запустить распознавание:
```sh
python -m src.main sample.png
```

Пример вывода:
[EAN13] 2465285613105
{'box_id': 'box-001', 'barcodes': [{'data': '2465285613105', 'type': 'EAN13'}]}


Несколько изображений имитируют кадры с разных граней одной коробки — коды
агрегируются и дедуплицируются:
```sh
python -c "import barcode; from barcode.writer import ImageWriter; barcode.get('ean13', '400638133393', writer=ImageWriter()).save('sample2')"
python -m src.main sample.png sample2.png
```

## Тесты

```sh
python -m pytest -q
```

## Структура
```
├── pytest.ini
├── README.md
├── report.md
├── requirements.txt
├── sample.png
├── sample2.png
├── SPEC.md
├── src
│   ├── __init__.py
│   ├── core
│   │   ├── __init__.py
│   │   └── processor.py
│   ├── main.py
│   ├── utils
│   │   ├── __init__.py
│   │   └── geometry.py
│   └── vision
│       ├── __init__.py
│       ├── decoder.py
│       └── detector.py
└── tests
    ├── __init__.py
    └── test_processor.py
```



## Ограничения демо

- Детектор YOLO - интерфейс-заглушка, обученная модель в комплект не входит.
- Коррекция перспективы и отправка результата по MQTT описаны в отчёте, но в
  демо не реализованы.
- Тестовые изображения - синтетические (чистые EAN-13), а не фото реальных коробок.
