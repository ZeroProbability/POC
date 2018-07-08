import groovy.beans.*
import java.util.concurrent.LinkedBlockingQueue

class Pixie {
    @Bindable Object value

    def eval() {
    }
}

class A extends Pixie {}
class B extends Pixie {}
class C extends Pixie {
    A a
    B b

    def eval() {
        this.value = a.value + b.value
    }
}

class D extends Pixie {
    C c
    B b

    def eval() {
        this.value = c.value + b.value
    }
}

class EventManager {
    {
        Thread.startDaemon {
            while(true) {
                def evt = events.take()
                println evt
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

a = new A(value: 1)
b = new B(value: 2)
c = new C(a : a, b: b)
d = new D(c : c, b: b)

evtManager.addPixie(a)
evtManager.addPixie(b)
evtManager.addPixie(c)
evtManager.addPixie(d)

println evtManager.notifyList
println c.getValue()
a.value = 10
println c.getValue()

Thread.sleep(1_000)
