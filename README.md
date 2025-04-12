# 🚀 Quick Route Finder

A Python-based route optimization tool that finds the **shortest path between cities** using **Dijkstra’s Algorithm** and **real-time distances** from the Google Maps Distance Matrix API.

---

## 🧠 Features

- 📍 Calculates shortest path between multiple user-defined locations.
- 🧭 Implements Dijkstra’s algorithm for accurate and efficient route optimization.
- 🌐 Uses Google Maps API to fetch real-time travel distances between cities.
- 💡 Simple command-line interface (CLI) — no web app or frontend needed!

---

## 🛠️ Technologies Used

- 🐍 Python 3
- 🔁 Dijkstra's Algorithm (Graph Theory)
- 🌍 Google Maps Distance Matrix API
- 🔗 Requests Library
- 📊 Data Structures (Dictionaries, Priority Queue)

---

## 📸 Demo

```bash
📍 Route Finder using Dijkstra + Google Maps API
Enter locations (comma-separated): Toronto, Ottawa, Mississauga, Vaughan, Montreal
Enter source location: Toronto
Enter destination location: Ottawa

📡 Fetching real distances between locations...
✅ Shortest path: Toronto → Vaughan → Ottawa
📏 Total distance: 448.8 km
