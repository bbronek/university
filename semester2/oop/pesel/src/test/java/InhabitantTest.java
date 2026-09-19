import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class InhabitantTest {
    @Test
    void storesFirstName() {
        Inhabitant inhabitant = new Inhabitant();
        inhabitant.setFirstName("John");
        assertEquals("John", inhabitant.getFirstName());
    }
}
