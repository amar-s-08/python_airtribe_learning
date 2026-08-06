class Inheritance {

    Pengine p = new Pengine();
    p.start();
    p.stop();

}

class Engine {
    public void start(){
        System.out.println("Starting Engine");
    }

    public void stop(){
        System.out.println("Stopping Engine");
    }
}

class Pengine extends Engine{
    public void start(){
        System.out.println("Starting Petrol Engine");
    }

    public void stop(){
        System.out.println("Stopping Petrol Engine");
    }
}