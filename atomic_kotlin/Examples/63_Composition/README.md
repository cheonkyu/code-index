# 63. Composition: 코드 재사용의 쉬운 방법

안녕하세요! 코틀린 프로그래밍 초보자 여러분, 오늘은 **Composition (구성)**에 대해 알아볼게요. 구성은 코드 재사용을 위한 또 다른 중요한 기법으로, 이해하기 쉽고 효과적인 방법이랍니다. 먼저, 코드 재사용이라는 큰 주제 아래에서 어떻게 구성이 활용되는지 함께 살펴보도록 하죠.

## 코드 재사용이란?

코드 재사용이란 이미 작성된 코드를 다시 활용하는 것을 말해요. 처음엔 단순히 코드를 복사해서 사용하는 것으로 생각할 수 있어요. 하지만 복사해서 사용하다 보면 문제가 생겨요:

- **유지보수의 어려움**: 코드를 여러 곳에 복사해두면 나중에 변경사항을 적용할 때 모든 복사본을 찾아야 하고, 일관되게 수정해야 하는 번거로움이 생깁니다.
- **수정의 일관성**: 모든 복사본에 동일한 변경사항을 적용해야 하는데, 이는 매우 피곤한 작업이 될 수 있어요.

### 구성의 장점

구성은 이러한 문제를 해결하는 방법 중 하나예요. 기존 클래스의 기능을 새로운 클래스에서 재사용할 수 있어요. 핵심은 **"기능을 재사용하면서도 기존 코드를 변형하지 않는 것"**이에요.

### 구성과 상속의 차이

#### 상속 (Inheritance)
- **관계**: `is-a` 관계 (예: "집은 건물이다")
- **사용 예**: `House : Building`
  ```kotlin
  package composition1

  interface Building
  interface Kitchen
  interface House : Building {
      val kitchen: Kitchen
  }
  ```

#### 구성 (Composition)
- **관계**: `has-a` 관계 (예: "집은 주방을 가지고 있다")
- **사용 예**: `House` 내부에 여러 `Kitchen` 객체를 가질 수 있음
  ```kotlin
  package composition3

  interface Building
  interface Kitchen
  interface House : Building {
      val kitchens: List<Kitchen>  // 여러 주방을 가질 수 있음
  }
  ```

### 초보자를 위한 구성 예시

#### 단순한 구성 예시
집 클래스에서 여러 주방을 관리하는 방법을 보세요:
```kotlin
package composition3

interface Building
interface Kitchen
interface House : Building {
    val kitchens: List<Kitchen>  // List를 사용해 여러 주방을 관리
}

// 실제 구현 예시
class KitchenImpl(val name: String) : Kitchen {
    override fun cook() = "주방 $name에서 요리 중"
}

class House : House {
    private val kitchens = mutableListOf<Kitchen>()

    fun addKitchen(kitchen: Kitchen) {
        kitchens.add(kitchen)
    }

    override fun kitchens(): List<Kitchen> {
        return kitchens
    }
}
```

### 구성과 상속 선택하기

- **구성**: 기존 클래스의 기능을 새로운 클래스에서 재사용할 수 있지만, 인터페이스는 새로 정의할 수 있어요.
- **상속**: 기존 클래스를 상속받아 인터페이스와 기능을 함께 물려받아요.

**구성을 선호하는 이유**:
- **간단한 디자인**: 복잡성을 줄이고 유지보수가 쉽습니다.
- **유연성**: 필요에 따라 클래스를 쉽게 조정할 수 있어요.

#### 예시: 객체 내부에 객체 포함하기
```kotlin
package composition

class Features {
    fun f1() = "feature1"
    fun f2() = "feature2"
}

class Form {
    private val features = Features()  // 내부 객체로 숨기기

    fun operation1() = features.f2() + features.f1()
    fun operation2() = features.f1() + features.f2()
}
```

### 주요 핵심 개념 요약
- **구성의 목적**: 기존 클래스의 기능을 새로운 클래스에서 재사용하되, 기존 코드를 직접 수정하지 않고 유지보수를 쉽게 하세요.
- **구성 vs 상속**: `has-a` 관계를 구성으로, `is-a` 관계를 상속으로 이해하세요. 구성은 더 유연하고 유지보수하기 쉬워요.
- **사용 사례**: 여러 주방을 가진 집 클래스를 통해 구성의 유용성을 확인할 수 있어요.

이제 구성에 대해 좀 더 친숙하게 느끼셨기를 바라요! 궁금한 점이 있으면 언제든지 물어보세요!