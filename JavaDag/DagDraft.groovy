import groovy.beans.*
import java.beans.*
import java.util.concurrent.LinkedBlockingQueue

class Pixie<T> {
    @Bindable T currentValue

    def eval() { }
}

class A extends Pixie<Integer> {}
class B extends Pixie<Integer> {
    A a

    @Override
    def eval() {
        this.currentValue = a.currentValue * a.currentValue
    }
}
class C extends Pixie<Integer> {
    A a

    def eval() {
        this.currentValue = a.currentValue * 2
    }
}

class D extends Pixie<Integer> {
    C c
    B b

    def eval() {
        this.currentValue = c.currentValue + b.currentValue + 1
    }
}

class E extends Pixie<Integer> {
    D d

    def eval() {
        this.currentValue = Math.sqrt(d.currentValue).intValue()
    }
}

class EventManager {
    {
        Thread.startDaemon {
            while(true) {
                def evt = events.take()
                if(notifyList.containsKey(evt.source)) {
                    def interestedPixies = notifyList[evt.source]
                    interestedPixies.each { l ->
                        l.eval()
                    }
                }
            }
        }
    }
    Queue events = new LinkedBlockingQueue()
    Pixie boundPixies = []

    Map<Pixie, List<Pixie>> notifyList=[:]

    void addPixie(Pixie p) {
        p.properties.findAll{k, v -> v instanceof Pixie }.each{ k, v ->
            if(notifyList.containsKey(v)) {
                notifyList.get(v).add(p)
            } else {
                notifyList[v] = [p]
            }
        }
        p.eval()

        p.propertyChange = {
            events.add(it)
        }
    }
}

evtManager = new EventManager()

a = new A(currentValue: 1)
b = new B(a: a)
c = new C(a: a)
d = new D(c: c, b: b)
e = new E(d: d)

evtManager.addPixie(a)
evtManager.addPixie(b)
evtManager.addPixie(c)
evtManager.addPixie(d)
evtManager.addPixie(e)

1.upto(10) {
    a.currentValue = it
    Thread.sleep(10)
    println "${it} => ${e.currentValue}"
}

