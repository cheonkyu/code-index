# 69. 중첩 클래스 (Nested Classes)

안녕하세요! 코틀린 프로그래밍을 처음 배우는 분들을 위해 중첩 클래스에 대해 친절하게 설명해드릴게요. 중첩 클래스는 코드 구조를 더욱 세밀하고 명확하게 만드는 데 도움이 되는 멋진 기능이에요. 지금부터 초보자분들도 쉽게 이해할 수 있도록 단계별로 설명해볼게요.

## 기본 개념 이해하기

### 중첩 클래스란 무엇인가요?

중첩 클래스는 **외부 클래스 내부에 정의된 클래스**입니다. 쉽게 말해, 하나의 큰 클래스 안에 작은 클래스를 포함시키는 거죠. 이렇게 하면 관련된 기능을 한 곳에 모아 코드를 더 깔끔하게 유지할 수 있어요.

### 예제 코드 살펴보기

#### 공항과 비행기 예시 (`Airport`와 `Plane`)

아래 코드는 `Airport`라는 외부 클래스 안에 `Plane`이라는 중첩 클래스를 정의한 예시입니다.

```kotlin
// 중첩클래스/Airport.kt
package nestedclasses
import atomictest.eq
import nestedclasses.Airport.Plane

class Airport(private val code: String) {
    // 중첩 클래스 Plane
    open class Plane {
        fun contact(airport: Airport) {
            println("Contacting ${airport.code}")  // 외부 클래스의 private 속성에 접근 가능
        }
    }

    // 중첩된 private 클래스 PrivatePlane
    private class PrivatePlane : Plane()

    fun privatePlane(): Plane = PrivatePlane()
}

fun main() {
    val denver = Airport("DEN")
    var plane = Plane()  // 중첩 클래스는 외부 클래스 없이도 생성 가능
    plane.contact(denver) eq "Contacting DEN"  // 성공!

    val frankfurt = Airport("FRA")
    plane = frankfurt.privatePlane()  // 중첩된 private 클래스 호출 가능
    plane.contact(frankfurt) eq "Contacting FRA"  // 성공!
}
```

**핵심 포인트:**
- **접근성:** `Plane` 클래스는 `Airport`의 `code` 같은 private 속성에 접근할 수 있어요. 일반 클래스였다면 불가능했을 거예요.
- **생성 방식:** 중첩 클래스는 외부 클래스 없이도 생성 가능하지만, 외부에서 중첩된 private 클래스를 직접 생성하는 건 제한적입니다 (`[2]` 부분 참조).

#### 청소 예시 (`Cleanable`과 하위 클래스들)

더 복잡한 중첩 구조를 보여주는 예시도 있어요. `Cleanable`이라는 추상 클래스로 `House`, `Bedroom`, `Closet`, `Shelf`, `Bathroom`, `Toilet`, `Sink` 등 여러 하위 클래스가 정의되어 있어요.

```kotlin
// 중첩클래스/NestedHouse.kt
package nestedclasses
import atomictest.*

abstract class Cleanable(val id: String) {
    open val parts: List<Cleanable> = listOf()
    fun clean(): String {
        if (parts.isEmpty()) return "$id clean"
        return "${parts.joinToString(
            " ", "(", ")",
            transform = Cleanable::clean)} $id clean\n"
    }
}

class House : Cleanable("House") {
    override val parts = listOf(
        Bedroom("Master Bedroom"),
        Bedroom("Guest Bedroom")
    )
}

class Bedroom(id: String) : Cleanable(id) {
    override val parts = listOf(Closet(), Bathroom())
}

class Closet : Cleanable("Closet") {
    override val parts = listOf(Shelf(), Shelf())
}

class Shelf : Cleanable("Shelf") {}

class Bathroom : Cleanable("Bathroom") {
    override val parts = listOf(Toilet(), Sink())
}

class Toilet : Cleanable("Toilet") {}

class Sink : Cleanable("Sink") {}

fun main() {
    House().clean() eq """
    (((Shelf clean Shelf clean) Closet clean
    (Toilet clean Sink clean) Bathroom clean
    ) Master Bedroom clean
    ((Shelf clean Shelf clean) Closet clean
    (Toile트 clean Sink clean) Bathroom clean
    ) Guest Bedroom clean
    ) House clean
    """
}
```

**핵심 포인트:**
- **다층 중첩:** 하위 클래스들이 서로 포함되어 복잡한 구조를 형성할 수 있어요. 각 클래스가 서로를 청소하는 방식으로 재귀적으로 작동해요.

## 중첩 클래스의 종류

### 내부 클래스 vs 외부 클래스

- **내부 클래스 (Nested Classes):** 외부 클래스 내부에 정의된 클래스입니다. 코드의 논리적 연관성을 높일 수 있어요.
- **로컬 클래스 (Local Classes):** 함수 내부에 정의된 클래스입니다. 일반적으로 함수의 특정 기능을 위한 클래스로 사용됩니다.

```kotlin
// 중첩클래스/LocalClasses.kt
package nestedclasses

fun localClasses() {
    open class Amphibian  // 일반 클래스로도 표현 가능하지만, 로컬 클래스 형태로도 사용 가능
    class Frog : Amphibian()
    val amphibian: Amphibian = Frog()  // 로컬 클래스 객체는 상위 클래스 타입으로 반환해야 함
}
```

**핵심 포인트:**
- **로컬 클래스 주의사항:** 일반적으로 로컬 클래스는 드물게 사용되며, 만약 큰 기능을 구현해야 한다면 일반 클래스로 정의하는 것이 더 좋습니다.

## 요약

- **중첩 클래스**는 코드 구조를 명확하게 만드는 데 유용해요. 관련 기능을 한 곳에 모아두면 이해하기 쉬워집니다.
- **접근성:** 중첩 클래스는 외부 클래스의 private 멤버에 접근할 수 있는 특별한 권한을 가지죠.
- **private 중첩 클래스:** 외부에서 직접 생성할 수는 없지만, 멤버 함수를 통해 접근 가능해요.
- **다층 구조:** 하위 클래스들이 서로 포함되어 복잡한 관계를 표현할 수 있어요.

이제 중첩 클래스에 대해 좀 더 자신감 있게 이해하고 적용할 수 있을 거예요! 궁금한 점이 있으면 언제든지 물어보세요! 😊