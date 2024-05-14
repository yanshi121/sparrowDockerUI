import docker


class DockerUIImage(object):
    def __init__(self):
        self.docker_env = docker.from_env()
    
    def refresh_docker_information(self):
        self.docker_env = docker.from_env()

    def docker_list_image(self):
        self.refresh_docker_information()
        images_infos_list = []
        try:
            images_list = self.docker_env.images.list()
            for image in images_list:
                images_infos_list.append({image.tags[0]: self.docker_get_image(image.tags[0])})
            return images_infos_list
        except Exception as e:
            return str(e)

    def docker_search_image(self, image_name: str):
        self.refresh_docker_information()
        images_list = self.docker_env.images.search(image_name)
        return images_list

    def docker_pull_image(self, image_name: str):
        self.refresh_docker_information()
        try:
            self.docker_env.images.pull(image_name)
            return True
        except Exception as e:
            return str(e)

    def docker_push_image(self, image_name: str):
        self.refresh_docker_information()
        try:
            self.docker_env.images.push(image_name)
            return True
        except Exception as e:
            return str(e)

    def docker_remove_image(self, image_name: str):
        self.refresh_docker_information()
        try:
            self.docker_env.images.remove(image_name)
            return True
        except Exception as e:
            return str(e)

    def docker_get_image(self, image_name: str):
        self.refresh_docker_information()
        try:
            image = self.docker_env.images.get(image_name)
            image_id = image.id
            image_attrs = image.attrs
            image_labels = image.labels
            image_short_id = image.short_id
            image_tags = image.tags[0]
            image_history = image.history()
            return {
                "image_id": image_id,
                "image_attrs": image_attrs,
                "image_labels": image_labels,
                "image_short_id": image_short_id,
                "image_tags": image_tags,
                "image_history": image_history
            }
        except Exception as e:
            return str(e)
if __name__ == '__main__':
    run = DockerUIImage()
    a = run.docker_get_image("python")
    import pprint; pprint.pprint(a)
    