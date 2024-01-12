import tkinter as tk

class Graph:
    def _init_(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]
    #heuristic cost of the nodes
    def h(self, n):
        H = {
            'Oradea': (380, 20),
            'Zerind': (374, 60),
            'Sibiu': (253, 150),
            'Arad': (366, 100),
            'Timisoara': (329, 140),
            'Lugoj': (244, 200),
            'Mehadia': (241, 250),
            'Dobreta': (242, 300),
            'Craiova': (160, 350),
            'Rimnicu Vilcea': (193, 200),
            'Pitesti': (30, 400),#10 to 30
            'Fagaras': (176, 180),
            'Bucharest': (40, 250),#0 to 40
            'Giurgiu': (77, 350),
            'Urziceni': (80, 400),
            'Vaslui': (199, 450),
            'Lasi': (226, 500),
            'Neamt': (234, 550),
            'Hirsova': (151, 450),
            'Eforie': (161, 500)
        }
        return H[n]

    def a_star_algorithm(self, start_node, stop_node):
        open_list = set([start_node])
        closed_list = set([])
        g = {}
        g[start_node] = 0
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None
            for v in open_list:
                if n is None or g[v] + self.h(v)[0] < g[n] + self.h(n)[0]:
                    n = v;

            if n is None:
                print('Path does not exist!')
                return None

            if n == stop_node:
                reconst_path = []
                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]
                reconst_path.append(start_node)
                reconst_path.reverse()
                print('Path found: {}'.format(reconst_path))
                return reconst_path

            for (m, weight) in self.get_neighbors(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None
#adjacency list describes how the nodes are connected with each other
adjacency_list = {
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Zerind': [('Oradea', 71), ('Arad', 75)],
    'Sibiu': [('Oradea', 151), ('Arad', 140), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Arad': [('Zerind', 75), ('Timisoara', 118), ('Sibiu', 140)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Dobreta', 75)],
    'Dobreta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Dobreta', 120), ('Pitesti', 138), ('Rimnicu Vilcea', 148)],
    'Rimnicu Vilcea': [('Craiova', 148), ('Sibiu', 80), ('Pitesti', 97)],
    'Pitesti': [('Craiova', 138), ('Rimnicu Vilcea', 97), ('Bucharest', 101)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Bucharest': [('Pitesti', 101), ('Fagaras', 211), ('Giurgiu', 90), ('Urziceni', 85)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
    'Vaslui': [('Urziceni', 142), ('Lasi', 92)],
    'Lasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Lasi', 87)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)]
}
class GraphGUI:
    def _init_(self, master, graph):
        self.master = master
        self.graph = graph
        self.canvas = tk.Canvas(self.master, width=800, height=600)
        self.canvas.pack()
        self.start_node = tk.StringVar()
        self.goal_node = tk.StringVar()
        
        start_label = tk.Label(self.master, text="Start Node:")
        start_label.place(x=10, y=10)
        start_menu = tk.OptionMenu(self.master, self.start_node, *graph.adjacency_list.keys())
        start_menu.place(x=100,y=10)

        goal_label = tk.Label(self.master, text="Goal Node:")
        goal_label.place(x=10, y=50)
        goal_menu = tk.OptionMenu(self.master, self.goal_node, *graph.adjacency_list.keys())
        goal_menu.place(x = 100, y = 50)

        find_path_button = tk.Button(self.master, text="Find Path", command=self.find_path)
        find_path_button.place(x = 10, y = 100)

    def find_path(self):
        start_node = self.start_node.get()
        goal_node = self.goal_node.get()

        if start_node and goal_node:
            path = self.graph.a_star_algorithm(start_node, goal_node)
            if path:
                self.draw_graph()
                self.draw_path(path)
            else:
                print("No path found.")

    def draw_graph(self):
    # Clear the canvas
        start_node = self.start_node.get()
        goal_node = self.goal_node.get()
        self.canvas.delete("all")

    # Draw nodes and edges
        for city, coordinates in self.graph.adjacency_list.items():
            
            x, y = self.graph.h(city)
            # Determine the color based on the node type
            node_color = 'lightblue'
            if city == start_node:
                node_color = 'Orange'
            elif city == goal_node:
                node_color = 'green'

        # Draw a circle for the node
            self.canvas.create_oval(x + 10, y + 10, x - 10, y - 10, fill=node_color)

        # Draw the city name at the node
            self.canvas.create_text(x, y, text=city)

        # Draw edges to neighbors
            for neighbor, weight in coordinates:
                x2, y2 = self.graph.h(neighbor)
                self.canvas.create_line(x, y, x2, y2)
            
            # Draw the weight of the edge
                label_x = (x + x2) / 2
                label_y = (y + y2) / 2
                self.canvas.create_text(label_x, label_y, text=str(weight), fill="blue")
    def draw_distances(self):
        drawn_labels = set()

        for city, neighbors in self.graph.adjacency_list.items():
            x1, y1 = self.graph.h(city)
            for neighbor, weight in neighbors:
                x2, y2 = self.graph.h(neighbor)
                label_x = (x1 + x2) / 2
                label_y = (y1 + y2) / 2

            # Ensure labels do not overlap
                while (label_x, label_y) in drawn_labels:
                    label_x += 30
                    label_y += 30

                self.canvas.create_line(x1, y1, x2, y2, fill="black", width=1)
                #self.canvas.create_text(label_x, label_y, text=str(weight), fill="black", font=("Arial", 10))
                drawn_labels.add((label_x, label_y))
    #draw path fuction draws the path between start and end nodes            
    def draw_path(self, path):
        for i in range(len(path) - 1):
            city1 = path[i]
            city2 = path[i + 1]
            x1, y1 = self.graph.h(city1)
            x2, y2 = self.graph.h(city2)
            self.canvas.create_line(x1, y1, x2, y2, fill="red", width=3)
        # Call the new method to draw the distances between cities
        self.draw_distances()        


graph1 = Graph(adjacency_list)
# Create the main window
root = tk.Tk()
root.title("A* Algorithm with GUI")
root.geometry("1000x800")
#root.configure(bg="black")

# Create an instance of the Graph class
graph = Graph(adjacency_list)

# Create an instance of the GraphGUI class, passing the main window and Graph instance
graph_gui = GraphGUI(root, graph)

# Start the Tkinter event loop
root.mainloop()
