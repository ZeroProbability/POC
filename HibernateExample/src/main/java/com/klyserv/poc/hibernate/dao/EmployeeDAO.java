package com.klyserv.poc.hibernate.dao;

import java.util.List;

import com.klyserv.poc.hibernate.entity.EmployeeEntity;

public interface EmployeeDAO {
	public void addEmployee(EmployeeEntity employee);

	public List<EmployeeEntity> getAllEmployees();

	public void deleteEmployee(Integer employeeId);
}