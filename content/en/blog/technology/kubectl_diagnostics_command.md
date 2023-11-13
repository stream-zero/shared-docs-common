---
title: "100 Kubernetes Diagnostics Commands with Kubectl"
linkTitle: "100 Kubernetes Diagnostics Commands with Kubectl"
tags: [kubectl, kubernetes, devops] 
categories: ["technology"]
weight: 101
description: >-
     Here is a list of 100 kubectl commands that can be useful for diagnosing issues in a Kubernetes cluster. These were prepared as a study aid for my CKAD exams with the help of ChatGPT.
---

Here is a list of 100 `kubectl` commands that can be useful for diagnosing issues in a Kubernetes cluster:

#### Cluster Information:
1.  Show the Kubernetes version: `kubectl version`
2.  Display cluster information: `kubectl cluster-info`
3.  List all nodes in the cluster: `kubectl get nodes`
4.  Describe a specific node: `kubectl describe node <node-name>`
5.  List all namespaces: `kubectl get namespaces`
6.  List all pods in all namespaces: `kubectl get pods --all-namespaces`

#### Pod Diagnostics:

7.  List pods in a specific namespace: `kubectl get pods -n <namespace>`
8.  Describe a pod: `kubectl describe pod <pod-name> -n <namespace>`
9.  View pod logs: `kubectl logs <pod-name> -n <namespace>`
10.  Tail pod logs: `kubectl logs -f <pod-name> -n <namespace>`
11.  Execute a command in a pod: `kubectl exec -it <pod-name> -n <namespace> -- <command>`

#### Deployment Diagnostics:
16. List all deployments in a namespace: `kubectl get deployments -n <namespace>`
17. Describe a deployment: `kubectl describe deployment <deployment-name> -n <namespace>`
18. View rollout status: `kubectl rollout status deployment/<deployment-name> -n <namespace>`
19. View rollout history: `kubectl rollout history deployment/<deployment-name> -n <namespace>`


#### Pod Health Checks:
12.  Check pod readiness: `kubectl get pods <pod-name> -n <namespace> -o jsonpath='{.status.conditions[?(@.type=="Ready")].status}'`
13.  Check pod events: `kubectl get events -n <namespace> --field-selector involvedObject.name=<pod-name>`

#### Service Diagnostics:
14. List all services in a namespace: `kubectl get svc -n <namespace>`
15. Describe a service: `kubectl describe svc <service-name> -n <namespace>`


####  StatefulSet Diagnostics:
20. List all StatefulSets in a namespace: `kubectl get statefulsets -n <namespace>`
21. Describe a StatefulSet: `kubectl describe statefulset <statefulset-name> -n <namespace>`

#### ConfigMap and Secret Diagnostics:
22. List ConfigMaps in a namespace: `kubectl get configmaps -n <namespace>`
23. Describe a ConfigMap: `kubectl describe configmap <configmap-name> -n <namespace>`
24. List Secrets in a namespace: `kubectl get secrets -n <namespace>`
25. Describe a Secret: `kubectl describe secret <secret-name> -n <namespace>`

####  Namespace Diagnostics:
26. Describe a namespace: `kubectl describe namespace <namespace-name>`

#### Resource Usage:
27. Check resource usage for a pod: `kubectl top pod <pod-name> -n <namespace>`
28. Check resource usage for nodes: `kubectl top nodes`

####  Networking Diagnostics:
29. Show the IP addresses of pods in a namespace: `kubectl get pods -n <namespace -o custom-columns=POD:metadata.name,IP:status.podIP --no-headers`
30. List all network policies in a namespace: `kubectl get networkpolicies -n <namespace>`
31. Describe a network policy: `kubectl describe networkpolicy <network-policy-name> -n <namespace>`

####  Persistent Volume (PV) and Persistent Volume Claim (PVC) Diagnostics:
32. List PVs: `kubectl get pv`
33. Describe a PV: `kubectl describe pv <pv-name>`
34. List PVCs in a namespace: `kubectl get pvc -n <namespace>`
35. Describe a PVC: `kubectl describe pvc <pvc-name> -n <namespace>`

#### Node Diagnostics:
36. Get the list of pods running on a specific node: `kubectl get pods --field-selector spec.nodeName=<node-name> -n <namespace>`

#### Resource Quotas and Limits:
37. List resource quotas in a namespace: `kubectl get resourcequotas -n <namespace>`
38. Describe a resource quota: `kubectl describe resourcequota <resource-quota-name> -n <namespace>`

#### Custom Resource Definitions (CRD) Diagnostics:
39. List custom resources in a namespace: `kubectl get <custom-resource-name> -n <namespace>`
40. Describe a custom resource: `kubectl describe <custom-resource-name> <custom-resource-instance-name> -n <namespace>`

Remember to replace `<namespace>`, `<pod-name>`, `<service-name>`, `<deployment-name>`, `<statefulset-name>`, `<configmap-name>`, `<secret-name>`, `<namespace-name>`, `<pv-name>`, `<pvc-name>`, `<node-name>`, `<network-policy-name>`, `<resource-quota-name>`, `<custom-resource-name>`, and `<custom-resource-instance-name>` with your specific values when using these commands. These commands should help you diagnose various aspects of your Kubernetes cluster and applications running within it.

#### Resource Scaling and Autoscaling:
41. Scale a deployment: `kubectl scale deployment <deployment-name> --replicas=<replica-count> -n <namespace>`
42. Set autoscaling for a deployment: `kubectl autoscale deployment <deployment-name> --min=<min-pods> --max=<max-pods> --cpu-percent=<cpu-percent> -n <namespace>`
43. Check horizontal pod autoscaler status: `kubectl get hpa -n <namespace>`

#### Job and CronJob Diagnostics:
44. List all jobs in a namespace: `kubectl get jobs -n <namespace>`
45. Describe a job: `kubectl describe job <job-name> -n <namespace>`
46. List all cron jobs in a namespace: `kubectl get cronjobs -n <namespace>`
47. Describe a cron job: `kubectl describe cronjob <cronjob-name> -n <namespace>`

#### Volume Diagnostics:
48. List persistent volumes (PVs) sorted by capacity: `kubectl get pv --sort-by=.spec.capacity.storage`
49. Check PV reclaim policy: `kubectl get pv <pv-name> -o=jsonpath='{.spec.persistentVolumeReclaimPolicy}'`
50. List all storage classes: `kubectl get storageclasses`

#### Ingress and Service Mesh Diagnostics:
51. List all ingresses in a namespace: `kubectl get ingress -n <namespace>`
52. Describe an ingress: `kubectl describe ingress <ingress-name> -n <namespace>`
53. List all VirtualServices (Istio) in a namespace: `kubectl get virtualservices -n <namespace>`
54. Describe a VirtualService (Istio): `kubectl describe virtualservice <virtualservice-name> -n <namespace>`

#### Pod Network Troubleshooting:
55. Run a network diagnostic pod (e.g., busybox) for debugging: `kubectl run -it --rm --restart=Never --image=busybox net-debug-pod -- /bin/sh`
56. Test connectivity from a pod to a specific endpoint: `kubectl exec -it <pod-name> -n <namespace> -- curl <endpoint-url>`
57. Trace network path from one pod to another: `kubectl exec -it <source-pod-name> -n <namespace> -- traceroute <destination-pod-ip>`
58. Check DNS resolution from a pod: `kubectl exec -it <pod-name> -n <namespace> -- nslookup <domain-name>`

#### Config and Resource Validation:
59. Validate a Kubernetes YAML file without applying it: `kubectl apply --dry-run=client -f <yaml-file>`
60. Validate a pod's security context and capabilities: `kubectl auth can-i list pods --as=system:serviceaccount:<namespace>:<serviceaccount-name>`

#### RBAC and Security:
61. List roles and role bindings in a namespace: `kubectl get roles,rolebindings -n <namespace>`
62. Describe a role or role binding: `kubectl describe role <role-name> -n <namespace>`

#### Service Account Diagnostics:
63. List service accounts in a namespace: `kubectl get serviceaccounts -n <namespace>`
64. Describe a service account: `kubectl describe serviceaccount <serviceaccount-name> -n <namespace>`

#### Node Drain and Uncordon:
65. Drain a node for maintenance: `kubectl drain <node-name> --ignore-daemonsets`
66. Uncordon a previously drained node: `kubectl uncordon <node-name>`

#### Resource Cleanup:
67. Delete a pod forcefully (not recommended): `kubectl delete pod <pod-name> -n <namespace> --grace-period=0 --force`

#### Pod Affinity and Anti-Affinity:
68. List pod affinity rules for a pod: `kubectl get pod <pod-name> -n <namespace> -o=jsonpath='{.spec.affinity}'`
69. List pod anti-affinity rules for a pod: `kubectl get pod <pod-name> -n <namespace> -o=jsonpath='{.spec.affinity.podAntiAffinity}'`

#### Pod Security Policies (PSP):
70. List all pod security policies (if enabled): `kubectl get psp`

#### Kubernetes Events:
71. View recent cluster events: `kubectl get events --sort-by=.metadata.creationTimestamp`
72. Filter events by a specific namespace: `kubectl get events -n <namespace>`

#### Node Troubleshooting:
73. Check node conditions: `kubectl describe node <node-name> | grep Conditions -A5`
74. List node capacity and allocatable resources: `kubectl describe node <node-name> | grep -E "Capacity|Allocatable"`

#### Ephemeral Containers (Kubernetes 1.18+):
75. Run an ephemeral debugging container: `kubectl debug -it <pod-name> -n <namespace> --image=<debug-image> -- /bin/sh`

#### Resource Metrics (Metrics Server required):
76. Get CPU and Memory usage for pods: `kubectl top pod -n <namespace>`

#### Kubelet Diagnostics:
77. View kubelet logs on a node: `kubectl logs -n kube-system kubelet-<node-name>`

#### Advanced Debugging with Telepresence:
78. Debug a pod with Telepresence: `telepresence --namespace <namespace> --swap-deployment <pod-name>`

#### Kubeconfig and Contexts:
79. List available contexts: `kubectl config get-contexts`
80. Switch to a different context: `kubectl config use-context <context-name>`

#### Pod Security Standards (PodSecurity admission controller):
81. List PodSecurityPolicy (PSP) violations: `kubectl get psp -A | grep -vE 'NAME|REVIEWED'`

#### Pod Disruption Budget (PDB) Diagnostics:
82. List all PDBs in a namespace: `kubectl get pdb -n <namespace>`
83. Describe a PDB: `kubectl describe pdb <pdb-name> -n <namespace>`

#### Resource Lock Diagnostics (if using resource locks):
84. List resource locks in a namespace: `kubectl get resourcelocks -n <namespace>`

#### Service Endpoints and DNS:
85. List service endpoints for a service: `kubectl get endpoints <service-name> -n <namespace>`
86. Check DNS configuration in a pod: `kubectl exec -it <pod-name> -n <namespace> -- cat /etc/resolv.conf`

#### Custom Metrics (Prometheus, Grafana):
87. Query Prometheus metrics: Use `kubectl port-forward` to access Prometheus and Grafana services to query custom metrics.

#### Pod Priority and Preemption:
88. List priority classes: `kubectl get priorityclasses`

#### Pod Overhead (Kubernetes 1.18+):
89. List overhead in a pod: `kubectl get pod <pod-name> -n <namespace> -o=jsonpath='{.spec.overhead}'`

#### Volume Snapshot Diagnostics (if using volume snapshots):
90. List volume snapshots: `kubectl get volumesnapshot -n <namespace>`
91. Describe a volume snapshot: `kubectl describe volumesnapshot <snapshot-name> -n <namespace>`

#### Resource Deserialization Diagnostics:


92. Deserialize and print a Kubernetes resource: `kubectl get <resource-type> <resource-name> -n <namespace> -o=json`

#### Node Taints:
93. List node taints: `kubectl describe node <node-name> | grep Taints`

#### Mutating and Validating Webhook Configurations:
94. List mutating webhook configurations: `kubectl get mutatingwebhookconfigurations`
95. List validating webhook configurations: `kubectl get validatingwebhookconfigurations`

#### Pod Network Policies:
96. List pod network policies in a namespace: `kubectl get networkpolicies -n <namespace>`

#### Node Conditions (Kubernetes 1.17+):
97. List node conditions: `kubectl get nodes -o custom-columns=NODE:.metadata.name,READY:.status.conditions[?(@.type=="Ready")].status -l 'node-role.kubernetes.io/worker='`

#### Audit Logs:
98. Retrieve audit logs (if enabled): Check your Kubernetes audit log configuration for the location of audit logs.

#### Node Operating System Details:
99. Get the node's OS information: `kubectl get node <node-name> -o jsonpath='{.status.nodeInfo.osImage}'`

#### List All Running Pods in All Namespaces (Short Command):
100. List all running pods in all namespaces in a short format: `kubectl get pods --all-namespaces`

These commands should cover a wide range of diagnostics scenarios in Kubernetes. Make sure to replace placeholders like `<namespace>`, `<pod-name>`, `<deployment-name>`, etc., with actual values specific to your cluster and use case.