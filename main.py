from collections import deque


class Social_graph:
    def __init__(self) -> None:
        self.social_graph = {
            'ви': ['друг1', 'друг2', 'друг3'],
            'друг1': ['друг4', 'друг5'],
            'друг2': ['друг6', 'друг7'],
            'друг3': ['друг8'],
            'друг4': ['друг7'],
            'друг5': [],
            'друг6': [],
            'друг7': ['друг8'],
            'друг8': []
        }

    def bfs(self, start_user) -> tuple:
        visited = set()
        queue = deque([(start_user, 0)])
        max_distance = 0
        farthest_user = None
        connected_users = []

        while queue:
            current_user, distance = queue.popleft()

            if distance > max_distance:
                max_distance = distance
                farthest_user = current_user

            connected_users.append((current_user, distance))

            for friend in self.social_graph[current_user]:
                if friend not in visited:
                    queue.append((friend, distance + 1))
                    visited.add(friend)

        return farthest_user, max_distance, connected_users


def main():
    social_network = Social_graph()
    farthest_user, distance, connected_users = social_network.bfs('ви')

    print(f"Максимально віддалений користувач: {farthest_user}")
    print(f"Відстань: {distance}")
    print("Список користувачів, з якими ви пов'язані:")
    for user, distance in connected_users:
        print(f"{user}: відстань {distance}")


if __name__ == '__main__':
    main()
