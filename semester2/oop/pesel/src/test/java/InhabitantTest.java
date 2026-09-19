import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

class InhabitantTest {
    @Test
    void storesFirstName() {
        Inhabitant inhabitant = new Inhabitant();
        inhabitant.setFirstName("John");
        assertEquals("John", inhabitant.getFirstName());
    }
}
