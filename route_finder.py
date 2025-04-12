import requests

API_KEY = "Your_API_key"  # Replace this with your actual key

def get_distance(origin, destination):
    url = "https://maps.googleapis.com/maps/api/distancematrix/json"
    params = {
        "origins": origin,
        "destinations": destination,
        "key": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        print(f"📍 Fetching: {origin} → {destination}")
        element = data["rows"][0]["elements"][0]

        status = element.get("status", "UNKNOWN")
        print(f"➡️  API status: {status}")

        if status != "OK":
            return float('inf')

        distance_km = element["distance"]["value"] / 1000
        return distance_km

    except Exception as e:
        print(f"❌ Error during API call for {origin} → {destination}: {e}")
        return float('inf')

def build_graph(locations):
    graph = {}
    for i in range(len(locations)):
        graph[locations[i]] = {}
        for j in range(len(locations)):
            if i != j:
                dist = get_distance(locations[i], locations[j])
                graph[locations[i]][locations[j]] = dist
    return graph

def dijkstra(graph, start, end):
    shortest_distances = {node: float('inf') for node in graph}
    shortest_distances[start] = 0
    previous_nodes = {}
    unvisited = set(graph.keys())

    while unvisited:
        current = min((node for node in unvisited), key=lambda node: shortest_distances[node])

        if current == end or shortest_distances[current] == float('inf'):
            break

        unvisited.remove(current)

        for neighbor, weight in graph[current].items():
            if weight == float('inf'):
                continue
            distance = shortest_distances[current] + weight
            if distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = distance
                previous_nodes[neighbor] = current

    path, current = [], end
    if current in previous_nodes or current == start:
        while current in previous_nodes:
            path.insert(0, current)
            current = previous_nodes[current]
        path.insert(0, current)

    return path, shortest_distances[end]

def main():
    print("📍 Route Finder using Dijkstra + Google Maps API")
    locations = input("Enter locations (comma-separated): ").strip().split(",")
    locations = [loc.strip() for loc in locations]

    source = input("Enter source location: ").strip()
    destination = input("Enter destination location: ").strip()

    print("\n📡 Fetching real distances between locations...")
    graph = build_graph(locations)

    print("🔎 Finding shortest path...\n")
    path, distance = dijkstra(graph, source, destination)

    if not path or distance == float('inf'):
        print("❌ Could not find a valid path.")
    else:
        print(f"✅ Shortest path: {' → '.join(path)}")
        print(f"📏 Total distance: {distance:.2f} km")

if __name__ == "__main__":
    main()
