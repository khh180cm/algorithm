"""
리스트 끝에 원소를 추가하거나 제거하기
- 상수 시간: O(1)
"""
AWS_SERVICES = ["EC2", "Beanstalk", "Fargate", "Lightsail"]

# 1. 마지막에 원소 추가
AWS_SERVICES.append("ElastiCache")
print(AWS_SERVICES)

# 2. 마지막 원소 반환
AWS_SERVICES.pop()
print(AWS_SERVICES)
