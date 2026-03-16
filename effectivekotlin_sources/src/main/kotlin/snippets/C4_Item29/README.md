# Item 29: 외부 API 래핑을 고려하라

안녕하세요! 코틀린 프로그래밍 전문가이자 친절한 강사입니다. 오늘은 Effective Kotlin의 Item 29, "외부 API 래핑을 고려하라"에 대해 함께 알아보려고 해요. 외부 API를 사용할 때 코틀린의 장점을 활용하여 더욱 안전하고 사용하기 편리하게 만들 수 있는 방법을 배울 수 있을 거예요.

## 외부 API 래핑이 필요한 이유

외부 API는 여러분이 직접 작성한 코드가 아니기 때문에 예상치 못한 문제(예: null 값, 예외, 일관성 없는 데이터 형식 등)를 발생시킬 수 있습니다. 이러한 문제를 직접 다루는 것은 코드를 복잡하게 만들고 유지보수를 어렵게 만들죠.

외부 API를 래핑(Wrapping)한다는 것은 여러분이 직접 제어할 수 없는 외부 API를 코틀린의 추상화를 통해 감싸서 사용하는 것을 의미합니다. 래핑을 통해 다음과 같은 이점을 얻을 수 있습니다.

* **안전성 향상:** 외부 API에서 발생할 수 있는 예외나 null 값을 안전하게 처리하여 코드의 안정성을 높일 수 있습니다.
* **가독성 향상:** 복잡한 외부 API 호출을 더 간결하고 명확하게 만들어 코드의 가독성을 높일 수 있습니다.
* **유연성 확보:** 외부 API의 변경에 유연하게 대응할 수 있도록 코드를 설계할 수 있습니다.
* **코틀린 스타일 준수:** 외부 API의 API 스타일과 상관없이 코틀린의 컨벤션을 따르는 코드를 작성할 수 있습니다.

## 래핑 방법

외부 API를 래핑하는 방법은 여러 가지가 있지만, 몇 가지 일반적인 패턴을 소개할게요.

1. **데이터 클래스 활용:** 외부 API에서 반환하는 데이터를 저장하는 데이터 클래스를 정의하여 데이터 형식을 일관성 있게 관리할 수 있습니다.
2. **확장 함수 활용:** 외부 API의 함수를 코틀린의 확장 함수로 감싸서 더 편리하게 사용할 수 있습니다.
3. **예외 처리:** 외부 API에서 발생할 수 있는 예외를 잡아서 코틀린에서 처리하거나, 더 의미있는 예외로 변환하여 전달할 수 있습니다.
4. **Null 안전 처리:** 외부 API에서 null 값을 반환할 수 있는 경우, 코틀린의 null 안전 기능을 활용하여 안전하게 처리할 수 있습니다.

## 예제

자, 이제 간단한 예제를 통해 외부 API 래핑을 어떻게 적용할 수 있는지 알아볼까요?

```kotlin
// 외부 API (예시) - 실제 API는 더 복잡할 수 있습니다.
class ExternalApiService {
    fun getUserName(userId: Int): String? {
        // API 호출 로직...
        return if (userId > 0) "External User $userId" else null
    }
}

// 래퍼 클래스
class UserApi {
    private val externalApiService = ExternalApiService()

    fun getUserName(userId: Int): String {
        val userName = externalApiService.getUserName(userId) ?: throw IllegalArgumentException("Invalid user ID: $userId")
        return userName
    }
}

fun main() {
    val userApi = UserApi()

    try {
        println(userApi.getUserName(1)) // External User 1
        println(userApi.getUserName(0)) // IllegalArgumentException 발생
    } catch (e: IllegalArgumentException) {
        println("Error: ${e.message}") // Error: Invalid user ID: 0
    }
}
```

위 예제에서 `ExternalApiService`는 외부 API를 나타내는 클래스입니다. `getUserName` 함수는 userId를 받아 사용자 이름을 반환하지만, userId가 유효하지 않으면 `null`을 반환할 수 있습니다.

`UserApi` 클래스는 `ExternalApiService`를 래핑하여 더 안전하고 사용하기 편리한 인터페이스를 제공합니다. `getUserName` 함수는 `ExternalApiService`에서 반환된 값이 `null`인 경우 `IllegalArgumentException`을 발생시켜 예외 처리를 수행합니다. 이렇게 함으로써, 외부 API의 잠재적인 문제를 래핑 클래스 내에서 처리하여 코드의 안정성을 높일 수 있습니다.

## 핵심 요약

* 외부 API를 래핑하면 코드의 안전성, 가독성, 유연성을 향상시킬 수 있어요.
* 데이터 클래스, 확장 함수, 예외 처리, null 안전 처리 등의 코틀린 기능을 활용해서 래핑을 구현할 수 있습니다.
* 외부 API의 잠재적인 문제를 래핑 클래스 내에서 처리하는 것이 중요합니다.
* 래핑을 통해 외부 API의 변경에 유연하게 대응할 수 있도록 코드를 설계하는 것이 좋습니다.