module sistema
    implicit none

contains
    subroutine sistema (t, t_inf, dydt, y, t_rec)
        !Parâmetros de entrada
        real(8), intent(in) :: t
        real(8), intent(in) :: t_inf
        real(8), intent(in) :: t_rec
        real(8), intent(in) :: y(3)
        
        real(8), intent(out) :: dydt

        