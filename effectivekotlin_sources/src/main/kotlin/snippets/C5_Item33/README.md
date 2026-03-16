# Item 33: 팩토리 함수 대신 생성자 사용 고려하기

## 핵심 가이드라인 및 이유

이 아이템에서는 클래스 생성에 있어서 전통적인 생성자 대신 팩토리 함수를 사용하는 방법을 살펴봅니다. 생성자는 코드의 가시성을 높이고 직접적인 인스턴스 생성을 허용하지만, 팩토리 함수를 활용하면 더 유연하고 안전한 인스턴스 생성을 가능하게 합니다. 주요 가이드라인과 그 이유는 다음과 같습니다:

1. **유연성 증가**: 팩토리 함수를 사용하면 생성 로직을 외부로 빼서 다양한 조건이나 파라미터에 따라 인스턴스를 생성할 수 있습니다. 이는 코드의 유연성을 크게 향상시킵니다.
   
2. **안전성 향상**: 복잡한 생성 로직이나 초기화 과정이 필요한 경우, 팩토리 함수를 통해 이러한 과정을 관리하면 코드의 오류 가능성을 줄일 수 있습니다. 예를 들어, 잘못된 입력에 대한 처리를 팩토리 함수 내에서 명확히 할 수 있습니다.

3. **코드 가독성**: 생성자 대신 명확한 이름의 팩토리 함수를 사용하면 호출 코드의 가독성을 높일 수 있습니다. 이는 특히 다양한 생성 옵션이 필요한 경우 더욱 유용합니다.

## 예제 코드

다음은 기본적인 예제를 통해 팩토리 함수와 생성자의 차이를 보여줍니다.

### 생성자 예시
```kotlin
class User(
    val username: String,
    val email: String
) {
    // 생성자 내의 기본 초기화 로직
    init {
        require(username.isNotEmpty()) { "사용자 이름은 비어있을 수 없습니다." }
    }
}

fun createUser(username: String, email: String): User {
    return User(username, email)
}
```

### 팩토리 함수 예시
```kotlin
class User(
    val username: String,
    val email: String
) {
    // 생성자 내의 기본 초기화 로직
    init {
        require(username.isNotEmpty()) { "사용자 이름은 비어있을 수 없습니다." }
    }

    companion object {
        // 다양한 조건에 따른 팩토리 함수 제공
        fun createAdminUser(username: String, email: String, role: String): User {
            require(role == "admin") { "사용자는 관리자 역할이어야 합니다." }
            return User(username, email)
        }

        fun createRegularUser(username: String, email: String): User {
            return User(username, email)
        }
    }
}

// 사용 예시
val adminUser = User.createAdminUser("admin", "admin@example.com", "admin")
val regularUser = User.createRegularUser("user", "user@example.com")
```

## 핵심 요약
- **팩토리 함수**는 다양한 생성 조건에 따라 유연하게 인스턴스를 생성할 수 있게 해줍니다.
- **안전성**을 높이고 **가독성**을 개선하여 코드 관리에 도움이 됩니다.
- **생성 로직 분리**를 통해 코드 유지보수와 확장성을 향상시킵니다.