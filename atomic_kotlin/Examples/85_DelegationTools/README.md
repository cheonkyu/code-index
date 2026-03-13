# 85. DelegationTools

안녕하세요! 오늘은 **DelegationTools**에 대해 배워볼게요. 이 주제는 Kotlin 프로그래밍에서 객체 간에 역할을 나누는 데 있어 매우 유용한 기법이에요. 쉽게 말해, 특정 기능을 다른 객체에게 위임하는 방법을 배워볼 거예요. 이 방법을 활용하면 코드를 더 간결하고 유연하게 만들 수 있어요. 함께 배워볼게요!

## 핵심 개념 요약

- **위임(Delegation)**: 한 객체가 자신의 책임 일부를 다른 객체에게 맡기는 것을 의미해요. 이렇게 하면 각 객체가 전문적인 역할만 수행하게 되어 코드의 유지보수와 확장성이 향상됩니다.
- **인터페이스와 추상 클래스**: 위임을 구현할 때 주로 사용되는 도구들이에요. 특정 기능을 정의하고 여러 구현체가 이를 받아들일 수 있게 해요.
- **Proxy 패턴**: 위임을 통해 중간자 역할을 하는 객체를 만들어 실제 작업을 다른 객체에게 넘기는 패턴이에요.

## 기본 예제 이해하기

### 예제 코드: 간단한 위임 예제

```kotlin
// 목표: 동물 소리를 재생하는 기능을 구현해보기로 했어요.
// 특정 동물의 소리를 직접 구현하는 대신, 추상 클래스를 사용해 위임해볼게요.

// 추상 클래스 정의하기: 동물 소리를 재생하는 기능을 정의해요.
abstract class AnimalSound {
    abstract fun makeSound(): String // 추상 메서드를 정의해요
}

// 개 클래스: 추상 클래스를 구현하고 특정 소리를 반환해요.
class Dog : AnimalSound() {
    override fun makeSound(): String {
        return "멍멍!"
    }
}

// 고양이 클래스: 추상 클래스를 구현하고 다른 소리를 반환해요.
class Cat : AnimalSound() {
    override fun makeSound(): String {
        return "냐옹~"
    }
}

// 위임을 처리하는 클래스: 여러 동물 소리를 유연하게 관리해요.
class SoundController {
    private val sounds: MutableList<AnimalSound> = mutableListOf()

    fun addSound(sound: AnimalSound) {
        sounds.add(sound)
    }

    fun playSounds() {
        sounds.forEach { sound ->
            println("동물 소리: ${sound.makeSound()}")
        }
    }
}

fun main() {
    val controller = SoundController()
    controller.addSound(Dog())
    controller.addSound(Cat())
    controller.playSounds() // 실행 결과: 멍멍! 냐옹~
}
```

### 코드 설명

1. **추상 클래스 `AnimalSound`**: `makeSound` 메서드를 정의해요. 이 메서드는 각 동물이 낼 소리를 반환해야 해요.
2. **구체 클래스 `Dog`와 `Cat`**: 각각 `makeSound` 메서드를 구현하여 실제 소리를 반환해요.
3. **`SoundController` 클래스**: 여러 `AnimalSound` 객체를 모아두고 `playSounds` 메서드를 통해 각각의 소리를 재생해요. 이 클래스가 위임의 핵심 역할을 해요.
4. **`main` 함수**: `SoundController` 객체를 생성하고 `Dog`와 `Cat` 객체를 추가한 후, 모든 동물의 소리를 재생해요.

이렇게 위임을 사용하면, 새로운 동물 소리를 추가하려면 단순히 새로운 클래스를 만들고 `SoundController`에 추가하면 되므로 코드를 쉽게 확장할 수 있어요. 이해하셨나요? 혹시 궁금한 점이 있으면 언제든지 물어보세요!