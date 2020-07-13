import kubernetes

k = kubernetes.client.models.V1ContainerStatus(image="ee", image_id="eee", name="eeee", ready=True,
                                               restart_count=0, state=kubernetes.client.models.V1ContainerState())
for f in dir(k):
    v = getattr(k, f, None)
    if hasattr(v, "to_dict"):
        try:
            print(v.to_dict())
        except Exception as e:
            print(type(e))
            continue