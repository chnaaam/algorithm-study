from collections import defaultdict


N = int(input())
addresses = []
for _ in range(N):
    addresses.append(input())

domain_dict = defaultdict(int)

for address in addresses:
    if address.startswith("http://"):
        address = address.replace("http://", "")

    domain = address.split("/")[0]
    if "." in domain:
        domain = domain.split(".")[-1]

    domain_dict[domain] += 1

sorted_domain_dict = sorted(domain_dict.items(), key=lambda x: x[1], reverse=True)
max_count = sorted_domain_dict[0][1]
max_domain_list = [sorted_domain_dict[0][0]]

for domain, count in sorted_domain_dict[1:]:
    if max_count == count:
        max_domain_list.append(domain)

print(max_count)
print(" ".join(max_domain_list))
