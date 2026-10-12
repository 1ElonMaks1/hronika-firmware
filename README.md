# Hronika Firmware Repository

Публичный репозиторий для OTA-обновлений рекордера Hronika CR-1.

## Что тут лежит

- `manifest.json` — описание актуальных версий прошивок
- Ссылки на `.bin` файлы — в разделе [Releases](../../releases)

## URL для приложения
https://1ElonMaks1.github.io/hronika-firmware/manifest.json

## Как выложить новую версию

1. Собрать прошивку в Arduino IDE → **Sketch → Export Compiled Binary**
2. Создать [New Release](../../releases/new) с тегом `audio-vX.Y.Z` или `ui-vX.Y.Z`
3. Прикрепить .bin как ассет, опубликовать
4. Посчитать SHA256: `shasum -a 256 audio.bin`
5. Обновить `manifest.json`, закоммитить, запушить
6. Через ~30 сек GitHub Pages отдаст обновлённый JSON
