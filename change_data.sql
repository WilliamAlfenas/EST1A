-- SQLite

--insert into coletas_paciente_tratamentos(paciente_id, forma_tratamento_id)
select id paciente_id, 5 forma_tratamento_id 
from coletas_paciente
where id not in (
    select paciente_id 
    from coletas_paciente_tratamentos
) or tratamento_id in (12, 13);

select * from coletas_paciente_tratamentos;
select * from coletas_forma_tratamento;
select * from coletas_tratamento;
