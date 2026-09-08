from PIL import Image, ImageDraw

# Crear imagen 1: Requirements Management System
img1 = Image.new("RGB", (800, 500), "#0d1117")
d1 = ImageDraw.Draw(img1)
d1.rectangle([(0, 0), (800, 500)], fill="#1a1f26")
d1.rectangle([(50, 80), (750, 150)], outline="#b2e2a2", width=3)
d1.text((200, 100), "REQUIREMENTS SYSTEM", fill="#b2e2a2")

# Simular tabla
d1.line([(50, 200), (750, 200)], fill="#306998", width=2)
d1.line([(50, 260), (750, 260)], fill="#306998", width=1)
d1.line([(50, 320), (750, 320)], fill="#306998", width=1)
d1.line([(50, 380), (750, 380)], fill="#306998", width=1)

d1.text((70, 210), "REQ-001: Authentication", fill="#c9d1d9")
d1.text((600, 210), "DONE", fill="#29a745")
d1.text((70, 270), "REQ-002: Database", fill="#c9d1d9")
d1.text((600, 270), "DONE", fill="#29a745")
d1.text((70, 330), "REQ-003: API", fill="#c9d1d9")
d1.text((600, 330), "IN PROGRESS", fill="#ffa500")

img1.save("public/assets/images/project1.jpeg", "JPEG", quality=85)

# Crear imagen 2: QA Testing Automation  
img2 = Image.new("RGB", (800, 500), "#0d1117")
d2 = ImageDraw.Draw(img2)
d2.rectangle([(0, 0), (800, 500)], fill="#1a1f26")
d2.rectangle([(50, 80), (750, 150)], outline="#43b02a", width=3)
d2.text((200, 100), "QA TEST AUTOMATION", fill="#43b02a")

d2.text((60, 200), "Tests Passed: 156/156", fill="#29a745")
d2.text((60, 260), "Coverage: 87.3%", fill="#b2e2a2")
d2.text((60, 320), "Execution Time: 2.4s", fill="#b2e2a2")
d2.text((60, 380), "Status: READY", fill="#43b02a")

# Barra de progreso
d2.rectangle([(60, 430), (750, 450)], outline="#43b02a", width=2)
d2.rectangle([(60, 430), (725, 450)], fill="#29a745")

img2.save("public/assets/images/project2.jpeg", "JPEG", quality=85)

# Crear imagen 3: BAsónicos - Concert Finder
img3 = Image.new("RGB", (800, 500), "#0d1117")
d3 = ImageDraw.Draw(img3)
d3.rectangle([(0, 0), (800, 500)], fill="#1a1f26")
d3.rectangle([(50, 70), (750, 140)], outline="#00d4aa", width=3)
d3.text((50, 90), "BASONICOS", fill="#00d4aa")
d3.text((700, 90), "GBA", fill="#00d4aa")

d3.text((60, 180), "Concert Finder - Gran Buenos Aires", fill="#c9d1d9")
d3.text((60, 220), "Go | TypeScript | React | PostGIS | Python", fill="#b2e2a2")
d3.text((60, 260), "Features: interactive map & geolocation", fill="#c9d1d9")
d3.text((60, 300), "Filters by artist and proximity", fill="#c9d1d9")
d3.text((60, 340), "Follow artists + push notifications", fill="#c9d1d9")

# Pin de mapa
d3.ellipse([(600, 240), (680, 320)], fill="#e0484e")
d3.polygon([(600, 320), (678, 320), (640, 370)], fill="#e0484e")
d3.ellipse([(632, 272), (652, 292)], fill="#fff")

d3.rectangle([(60, 430), (750, 450)], outline="#00d4aa", width=2)
d3.text((290, 433), "PRODUCTION - Deployed on Render", fill="#00d4aa")

img3.save("public/assets/images/project-basonicos.jpeg", "JPEG", quality=85)

print("✓ Imágenes generadas exitosamente!")
print("  - project1.jpeg")
print("  - project2.jpeg")
print("  - project-basonicos.jpeg")
