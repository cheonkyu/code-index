# 87. LateInitialization: 늦은 초기화 이해하기

안녕하세요! 코틀린 프로그래밍을 처음 접하는 분들을 위해 늦은 초기화(`lateinit`)에 대해 쉽게 설명해드릴게요. 늦은 초기화는 클래스 생성 후에 특정 메서드 내에서만 초기화를 진행하고 싶을 때 유용한 기능이에요. 특히 라이브러리나 프레임워크에서 요구하는 특정 초기화 메서드를 구현할 때 정말 도움이 됩니다.

## 기본 개념

### 늦은 초기화란?

`lateinit`은 클래스 내에서 초기화 시기를 뒤로 미루는 방법입니다. 즉, 생성자에서 바로 초기화하지 않고, 나중에 필요한 시점에 초기화할 수 있게 해줍니다. 이렇게 하면 생성자에서 복잡한 초기화 로직을 피하고, 필요할 때만 초기화를 진행할 수 있어요.

### 예시: `Bag` 인터페이스와 `Suitcase` 클래스

예를 들어, `Bag` 인터페이스는 `setUp()` 메서드를 통해 인스턴스를 초기화하도록 요구한다고 가정해봅시다. `Suitcase` 클래스는 이 인터페이스를 구현하고, `setUp()` 메서드 내에서만 `items` 변수를 초기화하려고 합니다.

```kotlin
// Bag 인터페이스
package lateinitialization
interface Bag {
    fun setUp()
}

// Suitcase 클래스 구현
package lateinitialization
import atomictest.eq

class Suitcase : Bag {
    private var items: String? = null  // 초기화 시 null 체크 필요

    override fun setUp() {
        items = "socks, jacket, laptop"  // 여기서 초기화
    }

    fun checkSocks(): Boolean {
        return items?.contains("socks") ?: false  // null 체크 필요
    }
}

fun main() {
    val suitcase = Suitcase()
    suitcase.setUp()
    println(suitcase.checkSocks())  // true 출력
}
```

여기서 `items` 변수는 생성자에서 초기화할 수 없으므로 `null` 체크를 계속 해줘야 합니다. 이런 번거로움을 해결하기 위해 `lateinit`을 사용할 수 있어요.

### `lateinit` 사용 예시: `BetterSuitcase` 클래스

`BetterSuitcase` 클래스에서는 `lateinit`을 사용해 생성자에서 초기화하지 않고 `setUp()` 메서드에서만 초기화합니다.

```kotlin
// BetterSuitcase 클래스 구현
package lateinitialization
import atomictest.eq

class BetterSuitcase : Bag {
    lateinit var items: String  // lateinit 적용

    override fun setUp() {
        items = "socks, jacket, laptop"  // 여기서 초기화
    }

    fun checkSocks(): Boolean {
        return "socks" in items  // null 체크 없이 안전하게 사용 가능
    }
}

fun main() {
    val suitcase = BetterSuitcase()
    suitcase.setUp()
    println(suitcase.checkSocks())  // true 출력
}
```

## 주요 핵심 요약

1. **생성 후 초기화**: 클래스 생성 후에만 초기화를 진행하고 싶을 때 사용합니다.
2. **생성자 피하기**: 생성자에서 초기화하지 않고 메서드 내에서 초기화 가능합니다.
3. **null 체크 필요성 감소**: `lateinit`을 사용하면 필요할 때만 초기화되므로 null 체크를 줄일 수 있어요.
4. **제한 사항**:
   - `val` 대신 `var` 프로퍼티에만 사용 가능합니다.
   - 기본 타입은 사용할 수 없어요.
   - 추상 클래스나 인터페이스 내의 프로퍼티에는 사용 불가능합니다.
   - 초기화되지 않은 경우 컴파일 오류 대신 런타임 예외가 발생합니다 (`UninitializedPropertyAccessException`).

### 런타임 예외 확인

`::` 연산자를 사용해 `lateinit` 프로퍼티가 초기화되었는지 확인할 수 있습니다:

```kotlin
// 초기화 확인 예시
package lateinitialization
import atomictest.*

class WithLate {
    lateinit var x: String

    fun status(): Boolean {
        return ::x.isInitialized  // 초기화 여부 확인
    }
}

fun main() {
    println(::y.isInitialized)  // y는 아직 초기화되지 않았으므로 false 출력
    y = "Ready"
    println(::y.isInitialized)  // true 출력

    val withLate = WithLate()
    println(withLate.status())  // false 출력
    withLate.x = "Set"
    println(withLate.status())  // true 출력
}
```

이렇게 `lateinit`을 활용하면 코드를 더 간결하고 안전하게 작성할 수 있어요. 이해가 잘 되셨나요? 궁금한 점이 있으면 언제든지 물어보세요!