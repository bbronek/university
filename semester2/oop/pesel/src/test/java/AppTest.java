import java.util.ArrayList;
import java.util.List;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class AppTest {
    @Test
    void validatesPeselFormatAndChecksum() {
        assertThrows(PeselException.class, () -> App.checkPesel("345"));
        assertThrows(PeselException.class, () -> App.checkPesel("abcdefghijk"));
        assertThrows(PeselException.class, () -> App.checkPesel("02070803629"));
        assertDoesNotThrow(() -> App.checkPesel("02070803628"));
        assertDoesNotThrow(() -> App.checkPesel("00000000000"));
    }

    @Test
    void updatesExistingInhabitant() {
        Inhabitant original = new Inhabitant();
        original.setPesel("02070803628");
        List<Inhabitant> inhabitants = new ArrayList<>();
        inhabitants.add(original);
        Inhabitant replacement = new Inhabitant();
        replacement.setPesel(original.getPesel());
        replacement.setFirstName("John");
        assertFalse(App.modifyData(replacement, inhabitants));
        assertEquals("John", original.getFirstName());
        assertEquals(1, inhabitants.size());
    }
}
