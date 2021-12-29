public class PeselException extends Exception {
    String msg;

    public PeselException(String msg) {
        this.msg = msg;
    }

    public String toString() {
        return "CustomException: " + msg;
    }
}