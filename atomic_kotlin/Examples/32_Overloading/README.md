# 32. Overloading: 여러 모습의 함수를 한 이름으로 부르기

안녕하세요! 오늘은 Kotlin에서 매우 유용한 기능 중 하나인 **오버로딩(Overloading)**에 대해 배워볼게요. 초보자분들도 쉽게 이해할 수 있도록 친근하게 설명해드릴게요.

## 무엇이 오버로딩일까요?

**오버로딩**이란 같은 이름의 함수를 여러 개 정의하는 것을 말해요. 하지만 중요한 건 각 함수의 **시그니처(signature)**가 다르다는 거예요. 시그니처란 함수의 이름, 매개변수 목록, 그리고 반환 타입을 포함해요. Kotlin은 이 시그니처를 기준으로 함수를 구분해요.

### 기본 개념 요약

- **시그니처**: 함수 이름 + 매개변수 목록 + 반환 타입
- **매개변수 목록 유일성**: 매개변수 목록이 다르면 오버로딩 가능 (반환 타입은 오버로딩할 수 없음)
- **목적**: 같은 작업을 다르게 수행할 수 있게 함으로써 코드를 더 명확하게 만드는 것

### 예제 코드 살펴보기

#### 기본 오버로딩 예시

```kotlin
package overloading
import atomictest.eq

class Overloading {
    // 매개변수가 없는 버전
    fun f(): Int = 0
    
    // 매개변수가 있는 버전
    fun f(n: Int): Int = n + 2
}

fun main() {
    val o = Overloading()
    o.f()  // 결과: 0
    o.f(11) // 결과: 13
}
```

위 코드에서 `Overloading` 클래스는 `f()`라는 이름을 가진 두 개의 함수를 정의하고 있어요. 하나는 매개변수가 없고, 다른 하나는 `Int` 타입의 매개변수를 받아요. 이렇게 하면 `f()`라는 이름으로 다양한 상황에 맞게 호출할 수 있어요.

#### 멤버 함수와 확장 함수의 관계

```kotlin
package overloading
import atomictest.eq

class My {
    // 클래스 멤버 함수
    fun foo(): Int = 0
}

// 확장 함수 정의 (매개변수 추가)
fun My.foo(i: Int): Int = i + 2

fun main() {
    My().foo() // 결과: 0
    My().foo(1) // 결과: 3
}
```

클래스 멤버 함수와 확장 함수를 오버로딩하여 사용할 수 있어요. 주의할 점은 멤버 함수가 이미 같은 시그니처를 가질 경우 확장 함수는 호출되지 않는다는 거예요. 하지만 확장 함수로 다른 매개변수를 추가해 오버로딩을 할 수 있어요.

### 디폴트 인수는 오버로딩 대신 사용하기

오버로딩을 디폴트 인수로 모방하는 것은 좋지 않아요. 예를 들어:

```kotlin
// 잘못된 방법: 오버로딩을 디폴트 인수로 대체
package withoutdefaultarguments
import atomictest.eq

fun f(n: Int) = n + 373
fun f() = f(0) // 문제: 이 함수는 항상 첫 번째 버전을 호출

fun main() {
    f() eq 373 // 올바르지만, 복잡해짐
}
```

대신 디폴트 인수를 사용하는 것이 더 간단해요:

```kotlin
// 올바른 방법: 디폴트 인수 사용
package withdefaultarguments
import atomictest.eq

fun f(n: Int = 0) = n + 373

fun main() {
    f() eq 373 // 디폴트 매개변수 사용
    f(5) eq 378 // 명시적 매개변수 사용
}
```

### 오버로딩의 장점

오버로딩의 주요 장점은 다음과 같아요:

- **명확성**: 같은 작업을 다양한 방식으로 수행할 수 있어 코드가 더 명확해집니다.
- **가독성**: 예를 들어, `add`라는 이름의 함수를 여러 타입(`Int`, `Double`)에 대해 정의할 수 있어요.

#### 예제: 다양한 타입의 덧셈 함수

```kotlin
package overloading
import atomictest.eq

fun addInt(i: Int, j: Int): Int = i + j
fun addDouble(i: Double, j: Double): Double = i + j
fun add(i: Int, j: Int): Int = i + j
fun add(i: Double, j: Double): Double = i + j

fun main() {
    addInt(5, 6) eq add(5, 6) // 결과: 같음
    addDouble(56.23, 44.77) eq add(56.23, 44.77) // 결과: 같음
}
```

위 코드에서 `add`라는 이름을 가진 여러 함수가 각각 다른 타입을 처리할 수 있어요. 이렇게 하면 코드가 훨씬 직관적이고 이해하기 쉬워져요.

### 결론

오버로딩은 함수 이름을 재사용하면서 다양한 매개변수 타입을 처리할 수 있게 해주는 강력한 도구예요. 이를 통해 코드의 가독성과 유지보수성을 크게 향상시킬 수 있답니다. 이제 여러분도 Kotlin에서 오버로딩을 활용해보세요! 질문이 있으면 언제든지 물어봐요. 함께 배우는 재미를 느껴보세요! 😊